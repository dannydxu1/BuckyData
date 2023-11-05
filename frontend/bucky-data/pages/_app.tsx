import { ChakraProvider } from "@chakra-ui/react";
import theme from "../theme"; // Import your custom Chakra UI theme here
import { AppProps } from "next/app"; 
import Layout from "@/components/Layout";

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <ChakraProvider theme={theme}>
        <Layout>
            <Component {...pageProps} />
        </Layout>
    </ChakraProvider>
  );
}

export default MyApp;
	