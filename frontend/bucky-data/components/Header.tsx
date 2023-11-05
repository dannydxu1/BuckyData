// components/Header.tsx
import {
  Box,
  Flex,
  Text,
  Heading,
  Button,
  useColorModeValue,
  HStack,
} from "@chakra-ui/react";

import Dropdown from "./Dropdown";

const Header = () => {
  const bgColor = useColorModeValue("white", "gray.800");

  const productItems = [
    { label: "Product 1", onClick: () => console.log("Product 1 clicked") },
    { label: "Product 2", onClick: () => console.log("Product 2 clicked") },
    // ... other product items
  ];

  const companyItems = [
    { label: "About Us", onClick: () => console.log("About Us clicked") },
    { label: "Careers", onClick: () => console.log("Careers clicked") },
    // ... other company items
  ];

  return (
    <Flex
      as="header"
      align="center"
      justify="space-between"
      wrap="wrap"
      padding="1rem"
      bg={bgColor}
      color="black"
      boxShadow="sm"
    >
      <Heading fontSize="lg" fontWeight="bold">
        Bucky<span style={{ color: "red" }}>Data</span>
      </Heading>
      <HStack spacing={0}>
        <Dropdown label="Course Search" items={productItems} />
        <Dropdown label="Grad Planner" items={companyItems} />
        <Dropdown label="Profile" items={productItems} />
      </HStack>
      <HStack spacing={0}>
        <Button variant="ghost">Login</Button>
        <Button variant="blackAlpha">Sign Up</Button>
      </HStack>
    </Flex>
  );
};

export default Header;
