import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App.tsx';
import { YMaps } from '@pbe/react-yandex-maps';
import { QueryClient, QueryClientProvider } from 'react-query';
import './index.css';

const queryClient = new QueryClient();
const apikey = import.meta.env.VITE_ENV_MAP;

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <QueryClientProvider client={queryClient}>
      <YMaps
        query={{
          apikey: apikey,
          load: 'GeoObjectCollection,Map,Placemark,Balloon,map.addon.balloon,geoObject.addon.balloon,route,geocode,coordSystem.geo,util.bounds',
        }}
      >
        <App />
      </YMaps>
    </QueryClientProvider>
  </React.StrictMode>
);
