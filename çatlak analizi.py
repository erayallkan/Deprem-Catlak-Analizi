import cv2

img = cv2.imread('duvar.jpg')

# Gri ton
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# filtreleme
filtered = cv2.medianBlur(gray, 5)

# Kenar tespiti
edges = cv2.Canny(filtered, 100, 200)

# Çatlak tespiti
contours, hierarchy = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    # Çatlak alanı
    area = cv2.contourArea(contour)
    # Çatlak genişliğini hesapla
    width = contour.shape[0]
    # Eğer çatlak 40 pikselden küçükse tehlike yok, büyükse tehlikeli
    if width < 40:
        cv2.drawContours(img, contour, -1, (0, 255, 0), 2)
        cv2.putText(img, "Tehlike Yok", (contour.ravel()[0], contour.ravel()[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)
    else:
        cv2.drawContours(img, contour, -1, (0, 0, 255), 2)
        cv2.putText(img, "Tehlikeli", (contour.ravel()[0], contour.ravel()[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)

# Kırmızı renk aralığı
lower_red = (0, 0, 200)
upper_red = (50, 50, 255)

# Kırmızı renk maskesi
mask = cv2.inRange(img, lower_red, upper_red)

# Maskenin alanı
mask_area = cv2.countNonZero(mask)

# Eğer kırmızı renk varsa metni fotoğrafa yazdır
if mask_area > 0:
    text_color = (0, 0, 255)
    # Metin stilini 
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    thickness = 3
    text = 'Uzmana kontrol ettirin'
    text_size, _ = cv2.getTextSize(text, font, font_scale, thickness)
    text_x = 5
    text_y = text_size[1]
    cv2.putText(img, text, (text_x, text_y), font, font_scale, text_color, thickness)
    
cv2.imshow('Tehlike Sonucu', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
