import { useQuery } from 'react-query';
import { fetchClosest } from './service';
import { Placemark } from '@pbe/react-yandex-maps';
import { currentCoords } from './App';

const ClosestBuses = ({ lat, long }: { lat: number; long: number }) => {
  const { isLoading: busesLoading, data: buses } = useQuery(`bus${lat}${long}`, () =>
    fetchClosest(...currentCoords)
  );
  console.log(lat, long);
  if (!busesLoading) console.log(buses);
  return (
    <>
      {buses
        ? buses.map((bus) => (
            <Placemark
              key={bus.id}
              geometry={[bus.lat, bus.long]}
              properties={{
                iconContent: `<div>${bus.bus_number}</div>`,
              }}
            />
          ))
        : null}
    </>
  );
};
export default ClosestBuses;
