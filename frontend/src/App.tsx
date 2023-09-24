import { Map, Placemark } from '@pbe/react-yandex-maps';

import SidePanel from './SidePanel';
import { FaceDetection } from './FaceDetection';
import { useState } from 'react';

export const currentCoords = [51.1200638, 71.46748] as const;

const App = () => {
  const [isFaceDetected, setIsFaceDetected] = useState(false);
  console.log(isFaceDetected);
  return (
    <>
      <FaceDetection isFaceDetected={isFaceDetected} setIsFaceDetected={setIsFaceDetected} />
      <Map
        defaultState={{
          center: currentCoords,
          zoom: 17,
        }}
        height={800}
        width={800}
      >
        <SidePanel active={isFaceDetected} />
        <Placemark
          geometry={currentCoords}
          options={{
            preset: 'islands#redIcon',
          }}
          properties={{
            balloonContent: '<div>You are here</div>',
          }}
        />
      </Map>
    </>
  );
};
export default App;
