import { useQuery } from 'react-query';
import { fetchStops } from './service';
import { Stop } from './types';
import { Clusterer, Placemark } from '@pbe/react-yandex-maps';
import { useState } from 'react';

const Stops = () => {
  const [selected, setSelected] = useState(-1);
  const { data: stops } = useQuery<Stop[][], Error>('stops', fetchStops);

  return (
    <>
      <Clusterer
        options={{
          preset: 'islands#blueDotIcon',
          groupByCoordinates: false,
        }}
      >
        {stops
          ? stops.flat().map((mark) => (
              <Placemark
                key={mark.id}
                geometry={[mark.lat, mark.long]}
                options={{
                  preset: 'islands#blueRailwayCircleIcon',
                  balloonAutoPan: true,
                  iconColor: selected == mark.id ? 'black' : 'blue',
                }}
                onClick={() => setSelected(mark.id)}
              />
            ))
          : null}
      </Clusterer>
    </>
  );
};
export default Stops;
