import { extendTheme } from '@chakra-ui/react';
import '@fontsource/merriweather';

const theme = extendTheme({
  colors: {
    uwRed: "#C5050C",
  },
  fonts: {
    // Define your custom fonts here
    body: 'Inter, sans-serif',
    heading: 'Merriweather, sans-serif',
  },
  // Customize other theme properties like spacing, typography, breakpoints, etc.
});

export default theme;
