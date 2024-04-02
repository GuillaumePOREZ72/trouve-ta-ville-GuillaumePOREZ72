import { createRoot } from 'react-dom/client';
import FindCity from './components/FindCity';

const container = document.querySelector("#app");

const root = createRoot(container);

root.render(<FindCity/>);