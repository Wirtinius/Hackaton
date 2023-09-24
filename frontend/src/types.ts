export type Coords = number[][];
export type Stop = {
  code: string;
  direction: boolean;
  id: number;
  lat: number;
  long: number;
  name: string;
  order: number;
};
export type Route = {
  id: string;
  bus_number: string;
  lat: string;
  long: string;
  direction: boolean;
};

export type Routes = {
  direction_true: Route[];
  direction_false: Route[];
};
