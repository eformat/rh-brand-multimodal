import { Analytics } from "@vercel/analytics/react";
import Header from "@/components/Header/Header";
import "./globals.css";
import Provider from "./Provider";
import Navbar from "@/components/Navbar/Navbar";
import SearchBox from "@/components/Search/SearchBox";

export const metadata = {
  title: "RedHat Icon Finder",
  description: "RedHat Icon Finder using next.js and tailwind css",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <Provider>
          {/* HEADER SECTION */}
          <Header />

          {/* NAVIGATION SECTION */}
          <Navbar />

          {/* SEARCH BOX */}
          <SearchBox />

          {children}
          {/*<Analytics /> */}
        </Provider>
      </body>
    </html>
  );
}
