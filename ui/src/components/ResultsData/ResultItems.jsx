import React from "react";
import Card from "../UI/Card";
import Link from "next/link";
import Image from "next/image";
import { FaRegThumbsUp } from "react-icons/fa";
import { AiFillStar } from "react-icons/ai";

const ResultItems = ({ results }) => {
  const image_url = process.env.IMAGE_URL || '0.0.0.0:5000';
  const image_prefix = process.env.IMAGE_PREFIX || 'http';
  return (
    <Card>
      <Link href={`/movie/${results.id}`}>
        <Image
          className="rounded-t-lg group-hover:opacity-70 transition-opacity duration-200"
          src={`${image_prefix}://${image_url}${
          results?.backdrop_path || results?.poster_path
          }`}
          width={500}
          height={300}
          style={{ maxWidth: "100%", maxHeight: "160px" }}
          placeholder="blur"
          blurDataURL="/spinner.svg"
          alt="Image is not available"
        />
        <div className="px-2">
          <p className="mt-2 line-clamp-2">{results?.overview}</p>
          <h2 className="word-break:break-all text-lg font-bold text-red-500 my-2">
            {results?.title || results?.original_title}
          </h2>
          <div className="flex justify-between items-center flex-wrap">
            {/* <p className="mt-1">{results?.release_date}</p> */}
            <p className="flex items-center mt-1 mx-1">
              <FaRegThumbsUp className="mr-1 text-red-500" />
              {results?.vote_count}
            </p>
            <p className="flex items-center mt-1">
              <AiFillStar className="text-amber-500 mr-1" />
              {Number(results?.vote_average).toFixed(1)}
            </p>
          </div>
        </div>
      </Link>
    </Card>
  );
};

export default ResultItems;
