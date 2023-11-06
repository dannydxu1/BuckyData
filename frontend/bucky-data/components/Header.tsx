import React, { useState } from "react";
import {
  Box,
  Flex,
  Heading,
  Button,
  MenuItem,
  Menu,
  MenuButton,
  MenuList,
  HStack,
  VStack,
  StackDivider,
  useColorModeValue,
  IconButton,
  Stack,
  Collapse,
  useDisclosure,
} from "@chakra-ui/react";
import {
  HamburgerIcon,
  ChevronDownIcon,
  SearchIcon,
  CloseIcon,
  ChevronRightIcon,
  CalendarIcon,
  ViewIcon,
  LockIcon,
  EditIcon,
} from "@chakra-ui/icons";


import Dropdown from "./Dropdown";
import MenuButtonLink from "./MenuButtonLink";

const Header = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const toggleMenu = () => setIsMenuOpen(!isMenuOpen);
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
    <Box>
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

        {/* Menu icon for mobile */}
        <IconButton
          size="md"
          icon={isMenuOpen ? <CloseIcon /> : <HamburgerIcon />}
          aria-label="Open Menu"
          display={{ md: "none" }}
          onClick={toggleMenu}
        />

        {/* Menu items hidden on mobile, shown on larger screens */}
        <HStack
          spacing={8}
          align="center"
          display={{ base: "none", md: "flex" }}
        >
          <Dropdown label="Course Search" items={productItems} />
          <Dropdown label="Grad Planner" items={companyItems} />
          <Dropdown label="Profile" items={productItems} />
        </HStack>

        <Flex align="center" display={{ base: "none", md: "flex" }}>
          <Button variant="ghost">Login</Button>
          <Button variant="blackAlpha">Sign Up</Button>
        </Flex>
      </Flex>

      <Collapse in={isMenuOpen} animateOpacity>
        <VStack
          p={4}
          display={{ md: "none" }}
          bg={bgColor}
          boxShadow="sm"
          divider={<StackDivider borderColor="gray.200" />} // Divider added
          spacing={4}
          align="stretch"
        >
          <MenuButtonLink>Course Search</MenuButtonLink>
          <MenuButtonLink>Grad Planner</MenuButtonLink>
          <MenuButtonLink>Profile</MenuButtonLink>
        </VStack>
      </Collapse>
    </Box>
  );
};

export default Header;
