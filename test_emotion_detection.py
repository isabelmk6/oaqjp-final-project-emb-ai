from EmotionDetection.emotion_detection import emotion_detector
import unittest


class TestEmotionDetector(unittest.TestCase):

    def test_emotion_detector(self):
        test_vals = {
            "I am glad this happened": "joy",
            "I am really mad about this": "anger",
            "I feel disgusted just hearing about this": "disgust",
            "I am so sad about this": "sadness",
            "I am really afraid that this will happen": "fear"
        }

        for k,v in test_vals.items():
            response = emotion_detector(k)
            dominant = response.get('dominant_emotion', '')
            self.assertEqual(dominant, v)


unittest.main()