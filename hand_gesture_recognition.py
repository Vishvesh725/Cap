{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a0f3b532-fd0c-4f48-83ef-47ad773e7715",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\vishv\\anaconda3\\Lib\\site-packages\\google\\protobuf\\symbol_database.py:55: UserWarning: SymbolDatabase.GetPrototype() is deprecated. Please use message_factory.GetMessageClass() instead. SymbolDatabase.GetPrototype() will be removed soon.\n",
      "  warnings.warn('SymbolDatabase.GetPrototype() is deprecated. Please '\n"
     ]
    },
    {
     "ename": "KeyboardInterrupt",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 21\u001b[0m\n\u001b[0;32m     19\u001b[0m \u001b[38;5;66;03m# Convert the BGR image to RGB\u001b[39;00m\n\u001b[0;32m     20\u001b[0m image_rgb \u001b[38;5;241m=\u001b[39m cv2\u001b[38;5;241m.\u001b[39mcvtColor(image, cv2\u001b[38;5;241m.\u001b[39mCOLOR_BGR2RGB)\n\u001b[1;32m---> 21\u001b[0m results \u001b[38;5;241m=\u001b[39m hands\u001b[38;5;241m.\u001b[39mprocess(image_rgb)\n\u001b[0;32m     23\u001b[0m \u001b[38;5;66;03m# Draw hand annotations on the image\u001b[39;00m\n\u001b[0;32m     24\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m results\u001b[38;5;241m.\u001b[39mmulti_hand_landmarks:\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\mediapipe\\python\\solutions\\hands.py:153\u001b[0m, in \u001b[0;36mHands.process\u001b[1;34m(self, image)\u001b[0m\n\u001b[0;32m    132\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mprocess\u001b[39m(\u001b[38;5;28mself\u001b[39m, image: np\u001b[38;5;241m.\u001b[39mndarray) \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m NamedTuple:\n\u001b[0;32m    133\u001b[0m \u001b[38;5;250m  \u001b[39m\u001b[38;5;124;03m\"\"\"Processes an RGB image and returns the hand landmarks and handedness of each detected hand.\u001b[39;00m\n\u001b[0;32m    134\u001b[0m \n\u001b[0;32m    135\u001b[0m \u001b[38;5;124;03m  Args:\u001b[39;00m\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m    150\u001b[0m \u001b[38;5;124;03m         right hand) of the detected hand.\u001b[39;00m\n\u001b[0;32m    151\u001b[0m \u001b[38;5;124;03m  \"\"\"\u001b[39;00m\n\u001b[1;32m--> 153\u001b[0m   \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28msuper\u001b[39m()\u001b[38;5;241m.\u001b[39mprocess(input_data\u001b[38;5;241m=\u001b[39m{\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mimage\u001b[39m\u001b[38;5;124m'\u001b[39m: image})\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\mediapipe\\python\\solution_base.py:340\u001b[0m, in \u001b[0;36mSolutionBase.process\u001b[1;34m(self, input_data)\u001b[0m\n\u001b[0;32m    334\u001b[0m   \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[0;32m    335\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_graph\u001b[38;5;241m.\u001b[39madd_packet_to_input_stream(\n\u001b[0;32m    336\u001b[0m         stream\u001b[38;5;241m=\u001b[39mstream_name,\n\u001b[0;32m    337\u001b[0m         packet\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_make_packet(input_stream_type,\n\u001b[0;32m    338\u001b[0m                                  data)\u001b[38;5;241m.\u001b[39mat(\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_simulated_timestamp))\n\u001b[1;32m--> 340\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_graph\u001b[38;5;241m.\u001b[39mwait_until_idle()\n\u001b[0;32m    341\u001b[0m \u001b[38;5;66;03m# Create a NamedTuple object where the field names are mapping to the graph\u001b[39;00m\n\u001b[0;32m    342\u001b[0m \u001b[38;5;66;03m# output stream names.\u001b[39;00m\n\u001b[0;32m    343\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_output_stream_type_info \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m: "
     ]
    }
   ],
   "source": [
    "import cv2\n",
    "import mediapipe as mp\n",
    "import numpy as np\n",
    "\n",
    "# Initialize MediaPipe Hands\n",
    "mp_hands = mp.solutions.hands\n",
    "hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)\n",
    "mp_drawing = mp.solutions.drawing_utils\n",
    "\n",
    "# Start video capture\n",
    "cap = cv2.VideoCapture(0)\n",
    "\n",
    "while True:\n",
    "    success, image = cap.read()\n",
    "    if not success:\n",
    "        print(\"Ignoring empty camera frame.\")\n",
    "        continue\n",
    "\n",
    "    # Convert the BGR image to RGB\n",
    "    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)\n",
    "    results = hands.process(image_rgb)\n",
    "\n",
    "    # Draw hand annotations on the image\n",
    "    if results.multi_hand_landmarks:\n",
    "        for hand_landmarks in results.multi_hand_landmarks:\n",
    "            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)\n",
    "\n",
    "            # Get the landmark positions\n",
    "            landmarks = hand_landmarks.landmark\n",
    "            # Example: Get the position of the index finger tip\n",
    "            index_finger_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]\n",
    "            h, w, _ = image.shape\n",
    "            index_finger_x, index_finger_y = int(index_finger_tip.x * w), int(index_finger_tip.y * h)\n",
    "\n",
    "            # Display the coordinates of the index finger tip\n",
    "            cv2.putText(image, f'Index Finger: ({index_finger_x}, {index_finger_y})', \n",
    "                        (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)\n",
    "\n",
    "    # Show the image\n",
    "    cv2.imshow('Hand Gesture Recognition', image)\n",
    "\n",
    "    # Break the loop on 'q' key press\n",
    "    if cv2.waitKey(1) & 0xFF == ord('q'):\n",
    "        break\n",
    "\n",
    "# Release the video capture object and close the windows\n",
    "cap.release()\n",
    "cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a2100856-4140-44bc-82de-f6f2afd768ab",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
