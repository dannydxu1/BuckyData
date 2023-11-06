import { Button } from "@chakra-ui/react";
import { ChevronRightIcon } from "@chakra-ui/icons";

const MenuButtonLink = ({ children, ...props }) => {
  return (
    <Button
      variant="ghost"
      w="full"
      h="1vhgh"
      justifyContent="space-between"
      rightIcon={<ChevronRightIcon />}
      {...props}
    >
      {children}
    </Button>
  );
};

export default MenuButtonLink;
