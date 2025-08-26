import React from "react";

const About = () => {
  return (
    <div className="max-w-6xl m-auto p-6 leading-relaxed">
      <h1 className="text-red-500 font-bold mb-4 text-3xl">About</h1>
      <div>
        <p>
          Welcome to the RedHat Icon Finder App. Search using natural language
          for you the icon you need. If you select the Name of the icon it will
          open the source image in your browser for easy download.
        </p>
        <p className="my-4">
          The icons are indexed and loaded from RedHat&apos;s Adobe suite. We use a
          vision language AI model to create text representations of each icon so
          that you can search against a late interaction model that runs on a GPU (its super fast !).
          Use the Search Keywords to hone in on the icons you want.
        </p>
        <p>
          Thank you for visiting the website and we hope you enjoy your time
          checking out all the icons. If you have any feedback or
          suggestions, please feel free to contact us.
        </p>
      </div>
    </div>
  );
};

export default About;
