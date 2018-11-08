import cv2
import matplotlib.pyplot as plt
import numpy as np
#便利Instagrmの広告用に写真をスプリットする

save_name = "insta_shikishima"
img = cv2.imread('Instagram_shikishima.jpg')
"""plt.imshow(img)
plt.show()"""

h, w, c = img.shape
v_split = 4  # 垂直方向の分割数
h_split = 3  # 水平方向の分割数

# 均等に分割できないと np.spllt() が使えないので、
# 除算したときに余りがでないように画像の端数を切り捨てる。
_img = img[:h // v_split * v_split, :w // h_split * h_split]
print('{} -> {}'.format(img.shape, _img.shape))  # (167, 292, 3) -> (164, 161, 3)

out_imgs = []
save_name = "insta_shikishima"
num = 1
for h_img in np.vsplit(_img, v_split):  # 垂直方向に分割する。
    for v_img in np.hsplit(h_img, h_split):  # 水平方向に分割する。
        out_imgs.append(v_img)
        cv2.imwrite('./split/'+str(num)+'_'+save_name+'.jpg', v_img)
        num +=1
out_imgs = np.array(out_imgs)
print(out_imgs.shape)  # (72, 24, 24, 3)

# 描画する。
"""fig, axes_list = plt.subplots(v_split, h_split, figsize=(5, 5))
axes_list = axes_list.ravel()
for i, (sub, axes) in enumerate(zip(out_imgs, axes_list)):
    axes.imshow(sub)
    axes.set_axis_off()
    axes.set_title(i)

plt.show()"""
