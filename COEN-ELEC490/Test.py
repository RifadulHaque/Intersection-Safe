import cv2

video = cv2.VideoCapture(0)


def Object():
    while (True):
        ret, frame = video.read()
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.realease()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    Object()
