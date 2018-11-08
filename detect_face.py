import cv2
import numpy as np
from pathlib import Path

# image : 画像配列
# face : 顔認識結果
# emoji : 使いたい絵文字画像。imreadの時に-1を指定してアルファチャンネル込で読み込む
# 返り値 : 絵文字を合成した画像
def pasteEmoji(image,face, emoji):
	resized_emoji = cv2.resize(emoji,(face[2],face[3])) #絵文字の画像サイズを顔の大きさに揃える

	# 透過処理
	# https://blanktar.jp/blog/2015/02/python-opencv-overlay.html
	mask = resized_emoji[:,:,3]
	mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
	mask = mask / 255.0 
	
	image = image.astype("float64") #予め型キャストしておく

	# 顔に画像を貼り付け
	image[face[1]:face[1]+face[2],face[0]:face[0]+face[3]] *= 1 -mask
	image[face[1]:face[1]+face[2],face[0]:face[0]+face[3]] += mask * resized_emoji[:,:,0:3]

	return image


# image : 顔認識を行いたい画像
# min_face_size_ratio : 顔の最小検出サイズを、画像の縦横短い方に対する比率で指定する。 0.0 ~ 1.0
# 返り値 : 顔認識結果の入った配列
def detectFaces(image, min_face_size_ratio):

	# カラーとグレースケールで画像サイズの取得を場合分けする
	if len(image.shape) == 3:
		height, width, _ = image.shape[:3]
	else:
		height, width = image.shape[:2]

	min_face_size = int(min(height, width) * min_face_size_ratio) # 顔の最小検出サイズ

	#グレースケール変換
	image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# 顔認識を実行
	cascade_path = "./cv2/data/haarcascade_frontalface_default.xml"
	cascade = cv2.CascadeClassifier(cascade_path)
	faces = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=2, minSize=(min_face_size, min_face_size))

	return faces


def main():

	# 先にアウトプットディレクトリを削除しておく
	outputs_path = Path("./outputs/")
	for file in outputs_path.iterdir():
		file.unlink()

	inputs_path = Path("./inputs/")

	for file in inputs_path.iterdir():
		image_file = str(file.name)
		image_path = inputs_path / image_file
		output_path = outputs_path / str(file.name)


		image = cv2.imread(str(image_path))
		faces = detectFaces(image, 0.12)


		for face in faces:

			angel = cv2.imread("emoji/angel.png",-1)
			image = pasteEmoji(image, face, angel)

		#認識結果の保存
		cv2.imwrite(str(output_path), image)


if __name__ == "__main__":
	main()
