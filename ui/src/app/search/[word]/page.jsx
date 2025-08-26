import Pagination from "@/components/Pagination/Pagination";
import Results from "@/components/ResultsData/Results";
import React from "react";

const Search = async ({ params, searchParams }) => {
  const searchWord = params.word;
  const pageNumber = searchParams.pageNumber || 1;
  const api_url = process.env.API_URL || '0.0.0.0:5000';

  const searchApi = await fetch(
    `http://${api_url}/search/${searchWord}?pageNumber=${pageNumber}`,
    { cache: 'no-store' }
  );

  if (!searchApi.ok) throw new Error("There is no icon with this keyword!");

  const data = await searchApi.json();

  return (
    <>
      <Results results={data?.results} />
      {data?.total_results >= 1 && (
        <Pagination totalPages={data?.total_pages} />
      )}
    </>
  );
};

export default Search;
