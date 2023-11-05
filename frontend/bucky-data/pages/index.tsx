
import { Heading, Box, Text, Button } from '@chakra-ui/react';

export default function Home() {
  return (
    <Box p={4} minH="95vh">
      <Heading as="h1" size="2xl" mb={4}>
        Welcome to My Next.js App
      </Heading>
      <Text fontSize="xl" mb={8}>
        This is a simple example home page for your Next.js app using Chakra UI.
      </Text>
      <Button colorScheme="blue">Get Started</Button>
    </Box>
  );
}