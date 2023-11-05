// components/Footer.js (or Footer.tsx)

import { Box, Text } from '@chakra-ui/react';

function Footer() {
  return (
    <Box as="footer" p={4} bg="gray.200" textAlign="center">
      <Text>&copy; {new Date().getFullYear()} Your Company Name</Text>
    </Box>
  );
}

export default Footer;
