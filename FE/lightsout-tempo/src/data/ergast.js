
export type RaceTable_type = {
    season: string;
    Races: Array;
};

export type MRData_def = {
    xmins: string;
    series: string;
    url: string;
    limit: string;
    offset: string;
    total: string;
    RaceTable: RaceTable_type;
};
export type ergast = { MRData: MRData_def }