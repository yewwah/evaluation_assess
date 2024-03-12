import React from "react";

import ElasticsearchAPIConnector from "@elastic/search-ui-elasticsearch-connector";

import {
  ErrorBoundary,
  Facet,
  SearchProvider,
  SearchBox,
  Results,
  PagingInfo,
  ResultsPerPage,
  Paging,
  Sorting,
  WithSearch
} from "@elastic/react-search-ui";
import { Layout } from "@elastic/react-search-ui-views";
import "@elastic/react-search-ui-views/lib/styles/styles.css";

import {
  buildAutocompleteQueryConfig,
  buildFacetConfigFromConfig,
  buildSearchOptionsFromConfig,
  buildSortOptionsFromConfig,
  getConfig,
  getFacetFields
} from "./config/config-helper";

const { hostIdentifier, searchKey, endpointBase, engineName } = getConfig();
const connector = new ElasticsearchAPIConnector({
  host: "http://localhost:9200",
  index: "cv-transcriptions"
});
const config = {
  searchQuery: {
    search_fields: {
      age: {
        weight: 3
      },
      gender: {},
      accent: {},
      generated_text: {},
      duration: {}
    },
    result_fields: {
      // filename,text,up_votes,down_votes,age,gender,accent,duration,generated_text
      filename: {
        snippet: {}
      },
      text: {
      },
      up_votes: {
      },
      down_votes: {
      },
      age:{
        snippet: {}
      },
      gender:{
        snippet: {}
      },
      duration:{
        snippet: {}
      },
      generated_text:{
        snippet: {}
      },
    },
    disjunctiveFacets: ["generated_text.keyword", "duration.keyword", "age.keyword", "gender.keyword", "accent.keyword"],
    facets: {
      "generated_text.keyword": { type: "value" },
      "duration.keyword": { type: "value" },
      "age.keyword": { type: "value" },
    }
  },
  autocompleteQuery: {
    results: {
      resultsPerPage: 5,
      search_fields: {
        "generated_text.suggest": {
          weight: 3
        },
        "age.suggest": {
          weight: 3
        },
        "duration.suggest": {
          weight: 3
        },
      },
      result_fields: {
        generated_text: {
          snippet: {
            size: 100,
            fallback: true
          }
        },
      }
    },
    suggestions: {
      types: {
        results: { fields: ["generated_text", "accent", "gender", "duration", "age"] }
      },
      size: 4
    }
  },
  apiConnector: connector,
  alwaysSearchOnInitialLoad: true
};

export default function App() {
  return (
    <SearchProvider config={config}>
      <WithSearch mapContextToProps={({ wasSearched }) => ({ wasSearched })}>
        {({ wasSearched }) => {
          return (
            <div className="App">
  <ErrorBoundary>
    <Layout
      header={
        <SearchBox
          autocompleteMinimumCharacters={3}
          autocompleteResults={{
            linkTarget: "_blank",
            sectionTitle: "Results",
            titleField: "generated_text",
            urlField: "url",
            shouldTrackClickThrough: true
          }}
          autocompleteSuggestions={true}
          debounceLength={0}
        />
      }
      sideContent={
        <div>
          {wasSearched && <Sorting label={"Sort by"} sortOptions={[]} />}
          <Facet key={"1"} field={"generated_text.keyword"} label={"generated_text"} />
          <Facet key={"2"} field={"age.keyword"} label={"age"} />
          <Facet key={"3"} field={"duration.keyword"} label={"duration"} />
          <Facet key={"4"} field={"gender.keyword"} label={"gender"} />
          <Facet key={"5"} field={"accent.keyword"} label={"accent"} />
        </div>
      }
      bodyContent={<Results shouldTrackClickThrough={true} />}
      bodyHeader={
        <React.Fragment>
          {wasSearched && <PagingInfo />}
          {wasSearched && <ResultsPerPage />}
        </React.Fragment>
      }
      bodyFooter={<Paging />}
    />
  </ErrorBoundary>
</div>
          );
        }}
      </WithSearch>
    </SearchProvider>
  );
}
