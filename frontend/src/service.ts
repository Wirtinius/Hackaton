import axios from 'axios';
import { Routes, Stop } from './types';

const URL = import.meta.env.VITE_ENV_URL;

export const fetchStops = async (): Promise<Stop[][]> => {
  const response = await axios.get(`${URL}/map/stops`, {
    headers: { 'ngrok-skip-browser-warning': true },
  });
  return response.data;
};

export const fetchRoute = async (id: number): Promise<Routes> => {
  const response = await axios.get(`${URL}/map/routes/${id}`, {
    headers: { 'ngrok-skip-browser-warning': true },
  });
  return response.data;
};

export const fetchBus = async (id: number): Promise<any> => {
  const response = await axios.get(`${URL}/map/buses/${id}`, {
    headers: { 'ngrok-skip-browser-warning': true },
  });
  return response.data;
};

export const fetchClosest = async (lat: number, long: number): Promise<any> => {
  const response = await axios.get(`${URL}/map/buses/?lat=${lat}&long=${long}`, {
    headers: { 'ngrok-skip-browser-warning': true },
  });
  return response.data;
};

export const sendToServer = async (file: FormData) => {
  if (!file) return;
  try {
    return await fetch(`${URL}/assistant/generate/`, { method: 'POST', body: file }).then((res) => {
      return res;
    });
  } catch (error) {
    console.log(error);
  }
};
