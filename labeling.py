from pydub import AudioSegment
from pydub.playback import play
import cv2
import glob
import imutils
import time

print('Welcome! 3 Second Mood Labeling Program...')

#input lagu
file = input('Lagu Nomor: ') 
sound = AudioSegment.from_file("audio_final/%s.mp3" % (file), format="mp3")
specto = cv2.imread("spectrogram_final/%s.png" % (file))

#definisi
one_sec_to_pixel = 12
in_second = 1000
three_sec_counter = 0
mood_kategori = ['undentified','Happy','Sad','Angry','Relaxed']

#log
log = 'filename: %s.mp3 ' % (file)
f = open('log.txt','a+')

#potong spectogram
h = specto.shape[0]
specto = specto[0:h,30*one_sec_to_pixel:60*one_sec_to_pixel] # y = atas ke bawah y+h = bawah ke bawah x = kiri ke kanan x+w = kiri ke kiri

#potong lagu
slices = sound[::30*in_second]
(potong1,potong2,potong3) = slices
slices = potong2[::3*in_second]

#memulai iterasi lagu 3 detik
print('Memulai memindai 3 detik ke mood...')
print('MOOD Category:\n(1) Happy,\n(2) Sad,\n(3) Angry,\n(4) relaxed,\n(5) belum yakin')
print('.')
time.sleep(2)
print('..')
time.sleep(2)
print('...')
time.sleep(2)
print('start:')
for i, chunk in enumerate(slices):
	#nomor potongan
	print(i+1)
	#play music
	play(chunk)
	#potong specto
	specto_potong= specto[0:h,three_sec_counter*one_sec_to_pixel:(three_sec_counter+3)*one_sec_to_pixel]
	#memindai kategori
	cat = int(input('Mood category (1-5): '))
	if cat != 5:
		labeling_loc = 'label/%s/%s-0%d.png' % (mood_kategori[cat],file,i+1)
		cv2.imwrite(labeling_loc,specto_potong)
	#saving log
	log = log+'| Mood%d: %s' % (i+1,mood_kategori[cat])
	#next function
	input('Pencet Enter untuk next 3 detik lagu...')
	three_sec_counter = three_sec_counter+3
print('END of Song')
f.write(log+'\n')
f.close()
print('Thankyou!')