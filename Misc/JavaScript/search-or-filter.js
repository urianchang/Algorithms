function findMatchingItems(toBeFiltered, toMatch, filterType, toBeMatched=null) {
  const filteredResults = toBeFiltered.filter((foo) => {
    if (filterType.toLowerCase() === 'search') {
      return toMatch.some((el) => foo[el].includes(toBeMatched));
    } else {
      //: When applying a filter, `toMatch` will be a dictionary
      return Object.keys(toMatch).some((k) => toMatch[k].includes(foo[k]));
    }
  });
  return filteredResults;
}

const streams = [
  {
    "stream": "asset_38:quality",
    "asset": "asset_38",
    "stream_type": "quality",
    "data_receiver": "receiver_1"
  },
  {
    "stream": "asset_42:bolts",
    "asset": "asset_42",
    "stream_type": "bolts",
    "data_receiver": "receiver_1"
  },
];

const searchParams = ['stream', 'asset', 'stream_type', 'data_receiver'];

const searchString = 'quality';

const filterBy = {
  'asset': ['asset_42']
};

const filterKeys = Object.keys(filterBy);

// const positiveMatches = findMatchingItems(streams, searchParams, 'search', searchString);
const positiveMatches = findMatchingItems(streams, filterBy, 'filter');
console.log(positiveMatches);
