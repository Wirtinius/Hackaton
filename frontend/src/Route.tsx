import { Placemark, Polyline } from '@pbe/react-yandex-maps';
import { useQuery } from 'react-query';
import { Routes } from './types';
import { fetchBus, fetchRoute } from './service';

const Route = ({ busId }: { busId: number }) => {
  const { isLoading: routesLoading, data: routes } = useQuery<Routes>(`route${busId}`, () =>
    fetchRoute(busId)
  );
  const { data: buses } = useQuery(`bus${busId}`, () => fetchBus(busId), {
    refetchInterval: 30000,
  });

  const routeCoordsTrue = routes
    ? routes.direction_true.map((route) => [+route.long, +route.lat])
    : [];
  const routeCoordsFalse = routes
    ? routes.direction_false.map((route) => [+route.long, +route.lat])
    : [];

  if (!routesLoading)
    console.log(routes?.direction_true.map((route) => [route.lat, route.long] as const));
  return (
    <>
      <Polyline
        geometry={routeCoordsTrue}
        options={{
          strokeColor: '#2563eb',
          strokeWidth: 4,
          strokeOpacity: 0.9,
        }}
      />
      <Polyline
        geometry={routeCoordsFalse}
        options={{
          strokeColor: '#2563eb',
          strokeWidth: 4,
          strokeOpacity: 0.4,
        }}
      />
      {buses
        ? buses.map((bus) => {
            return (
              <Placemark
                key={bus.id}
                geometry={[bus.lat, bus.long]}
                properties={{
                  iconContent: `<div>${bus.bus_number}</div>`,
                }}
              />
            );
          })
        : null}
    </>
  );
};
export default Route;
