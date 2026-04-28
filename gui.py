import cv2
from detector import detect

def run():
    cap = cv2.VideoCapture(0)

    print("🚗 System Running... Press Q to Exit")

    total_sleep = 0
    age_list = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame, sleep_count, ages = detect(frame)

        total_sleep = sleep_count
        age_list = ages

        cv2.imshow("Drowsiness Detection System", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    # FINAL OUTPUT
    print("\n===== FINAL OUTPUT =====")
    print("Sleeping People:", total_sleep)
    print("Ages:", age_list)

    if total_sleep > 0:
        print("⚠ ALERT: Drowsiness Detected!")
    else:
        print("✔ ALL CLEAR")

if __name__ == "__main__":
    run()