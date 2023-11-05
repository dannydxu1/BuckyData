// components/Dropdown.tsx
import React from 'react';
import {
  Menu,
  MenuButton,
  MenuList,
  MenuItem,
  Button,
  MenuProps,
} from '@chakra-ui/react';
import { ChevronDownIcon } from '@chakra-ui/icons';

type DropdownItem = {
  label: string;
  onClick: () => void;
};

type DropdownProps = {
  label: string;
  items: DropdownItem[];
  menuProps?: MenuProps; // Allows customization of the Menu component
};

const Dropdown: React.FC<DropdownProps> = ({ label, items, menuProps }) => {
  return (
    <Menu {...menuProps}>
      <MenuButton as={Button} rightIcon={<ChevronDownIcon />} variant="ghost">
        {label}
      </MenuButton>
      <MenuList>
        {items.map((item, index) => (
          <MenuItem key={index} onClick={item.onClick}>
            {item.label}
          </MenuItem>
        ))}
      </MenuList>
    </Menu>
  );
};

export default Dropdown;
