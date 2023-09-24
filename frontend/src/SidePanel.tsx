import { useState } from 'react';
import { AudioRecorder } from 'react-audio-voice-recorder';
import Route from './Route';
import { sendToServer } from './service';

import ClosestBuses from './ClosestBuses';

const SidePanel = ({ active }: { active: boolean }) => {
  const [route, setRoute] = useState<number>(0);
  const [closest, setClosest] = useState(false);
  const addAudioElement = async (blob: Blob) => {
    const formData = new FormData();
    formData.append('audio_file', blob, 'audio.wav');
    const result = await sendToServer(formData);
    if (result) {
      const parsed = JSON.parse(await result.text());
      console.log(parsed);
      if (parsed.function == 'get_closest_buses') {
        setRoute(0);
        setClosest(true);
      } else if (parsed.function == 'get_bus_route') {
        const bus = JSON.parse(parsed.args);
        setClosest(false);
        setRoute(bus.bus_number);
      } else if (parsed.function == 'message') {
        alert(parsed.args);
      } else if (parsed.function == 'videocall') {
        window.location.href = "http://localhost:8000/assistant/video";
      }
    }
  };

  return (
    <div>
      {active && (
        <div
          style={{
            position: 'absolute',
            right: 500,
            top: 30,
            width: 100,
            height: 100,
            display: 'flex',
            flexDirection: 'row',
            alignItems: 'stretch',
          }}
        >
          <AudioRecorder
            onRecordingComplete={addAudioElement}
            audioTrackConstraints={{
              noiseSuppression: true,
              echoCancellation: true,
            }}
          />
        </div>
      )}

      {route > 0 ? <Route busId={route} /> : null}
      {closest ? <ClosestBuses lat={51.1200638} long={71.46748} /> : null}
    </div>
  );
};
export default SidePanel;
