import { useEffect, useRef, useState } from 'react';
import Webcam from 'react-webcam';
import { draw } from './utils';
import * as blazeface from '@tensorflow-models/blazeface';

export const FaceDetection = ({
  isFaceDetected,
  setIsFaceDetected,
}: {
  isFaceDetected: boolean;
  setIsFaceDetected: React.Dispatch<React.SetStateAction<boolean>>;
}) => {
  const webcamRef = useRef(null);
  const canvasRef = useRef(null);
  const [lastDetectionTime, setLastDetectionTime] = useState<Date>();

  const returnTensors = false;

  useEffect(() => {
    const runFacedetection = async () => {
      const model = await blazeface.load();
      console.log('FaceDetection Model is Loaded..');
      setInterval(() => {
        detect(model);
      }, 1000);
      setInterval(() => {
        if (!isFaceDetected && lastDetectionTime !== null) {
          const currentTime = Date.now();
          const elapsedTime = currentTime - lastDetectionTime;
          if (elapsedTime >= 5000) {
            window.location.reload();
          }
        }
      }, 1000);
    };

    const detect = async (model) => {
      if (
        typeof webcamRef.current !== 'undefined' &&
        webcamRef.current !== null &&
        webcamRef.current.video.readyState === 4
      ) {
        // Get video properties
        const video = webcamRef.current.video;
        const videoWidth = webcamRef.current.video.videoWidth;
        const videoHeight = webcamRef.current.video.videoHeight;

        // Set video height and width
        webcamRef.current.video.width = videoWidth;
        webcamRef.current.video.height = videoHeight;

        // Set canvas height and width
        canvasRef.current.width = videoWidth;
        canvasRef.current.height = videoHeight;

        // Make detections
        const prediction = await model.estimateFaces(video, returnTensors);

        if (prediction.length > 0 && !isFaceDetected) {
          console.log('Face detected!');
          setIsFaceDetected(true);
          setLastDetectionTime(Date.now());
          // timeoutId = setTimeout(() => {
          //   setIsFaceDetected(false);
          // }, 10000);
        } else {
          setIsFaceDetected(false);
        }

        const ctx = canvasRef.current.getContext('2d');
        draw(prediction, ctx);
      }
    };

    runFacedetection();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <Webcam
          ref={webcamRef}
          style={{
            position: 'absolute',
            marginLeft: 'auto',
            marginRight: 'auto',
            top: 0,
            right: 0,
            textAlign: 'center',
            zIndex: 9,
            width: 320,
            height: 240,
          }}
        />

        <canvas
          ref={canvasRef}
          style={{
            position: 'absolute',
            marginLeft: 'auto',
            marginRight: 'auto',
            top: 0,
            right: 0,
            textAlign: 'center',
            zIndex: 9,
            width: 320,
            height: 240,
          }}
        />
      </header>
    </div>
  );
};
