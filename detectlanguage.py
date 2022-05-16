
import csv
from googletrans import Translator

detector = Translator()
dec_lan = detector.detect('ruchi')
print(dec_lan)
