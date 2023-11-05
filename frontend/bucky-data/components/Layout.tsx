// components/Layout.tsx

import { Box, Container, BoxProps } from '@chakra-ui/react';
import Header from './Header';
import Footer from './Footer';

interface LayoutProps extends BoxProps {
  children: React.ReactNode;
}

function Layout({ children, ...rest }: LayoutProps) {
  return (
    <Box minH="100vh"
     {...rest}>
      <Header />
      <Container maxW="container.lg" pt={4}>
        {children}
      </Container>
      <Footer />
    </Box>
  );
}

export default Layout;
