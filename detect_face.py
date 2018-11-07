import cv2
import numpy as np
from pathlib import Path

path = Path("./outputs/")

for file in path.iterdir():
	file.unlink()


path = Path("./inputs/")


for file in path.iterdir():

	cascade_path = "./cv2/data/haarcascade_frontalface_default.xml"
	# cascade_path = "./cv2/data/haarcascade_frontalface_alt.xml"
	# cascade_path = "./cv2/data/haarcascade_frontalface_alt2.xml"
	# cascade_path = "./cv2/data/haarcascade_frontalface_alt_tree.xml"
	# cascade_path = "./cv2/data/haarcascade_frontalface_alt_tree.xml"

	image_file = str(file.name)
	image_path = "./inputs/" + image_file
	output_path = "./outputs/" + str(file.name)

	#ファイル読み込み
	image = cv2.imread(image_path)
	# カラーとグレースケールで場合分け
	if len(image.shape) == 3:
		height, width, channels = image.shape[:3]
	else:
		height, width = image.shape[:2]
		channels = 1

	min_image_size = min(height, width)
	print(min_image_size)

	# 顔の最小サイズを決める
	min_face_size = int(min_image_size * 0.12)

	#グレースケール変換
	image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	#カスケード分類器の特徴量を取得する
	cascade = cv2.CascadeClassifier(cascade_path)

	faces = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=2, minSize=(min_face_size, min_face_size))

	print(faces)
	color = (255, 255, 255) #白

	# 検出した場合
	if len(faces) > 0:

		#検出した顔を囲む矩形の作成
		for face in faces:

			# 透過処理
			# https://blanktar.jp/blog/2015/02/python-opencv-overlay.html
			angel = cv2.imread("emoji/angel.png",-1)

			resized_angel = cv2.resize(angel,(face[2],face[3]))
			mask = resized_angel[:,:,3]
			mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
			mask = mask / 255.0 
			
			image = image.astype("float64")
			print(resized_angel.shape)

			image[face[1]:face[1]+face[2],face[0]:face[0]+face[3]] *= 1 -mask
			image[face[1]:face[1]+face[2],face[0]:face[0]+face[3]] += mask * resized_angel[:,:,0:3]
			#認識結果の保存
			cv2.imwrite(output_path, image)