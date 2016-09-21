app.factory('StatsFactory', function($http, apiUrl) {

    let Stats;

    return {

        // Scores
        fetchWinsByNight: () => {
            return $http.get(`${apiUrl}/winsby/night/`)
        },

        fetchWinsByAge: () => {
            return $http.get(`${apiUrl}/winsby/age/`)
        },

        fetchWinsByMrtlStat: () => {
            return $http.get(`${apiUrl}/winsby/mrtlstat/`)
        },

        fetchAvgWinScore: () => {
            return $http.get(`${apiUrl}/scores/avgwin/`)
        },

        fetchAvgScoreOverall: () => {
            return $http.get(`${apiUrl}/scores/avgoverall/`)
        },

        fetchAvgCoupleVote: () => {
            return $http.get(`${apiUrl}/scores/avgcouple/`)
        },

        fetchHighestScore: () => {
            return $http.get(`${apiUrl}/scores/highest/`)
        },

        fetchLowestScore: () => {
            return $http.get(`${apiUrl}/scores/lowest/`)
        },

        fetchHighestLosingScore: () => {
            return $http.get(`${apiUrl}/scores/highlosing/`)
        },

        fetchLowestWinningScore: () => {
            return $http.get(`${apiUrl}/scores/lowwinning/`)
        },


        // Entrees
        fetchEntreeProteinWinners: () => {
            return $http.get(`${apiUrl}/entree/proteinwinners/`)
        },

        fetchEntreeProteinOverall: () => {
            return $http.get(`${apiUrl}/entree/proteinoverall/`)
        },

        fetchEntreeProteinStyleWinners: () => {
            return $http.get(`${apiUrl}/entree/proteinstylewinners/`)
        },

        fetchEntreeProteinStyleOverall: () => {
            return $http.get(`${apiUrl}/entree/proteinstyleoverall/`)
        },

        fetchEntreeSideWinners: () => {
            return $http.get(`${apiUrl}/entree/sidewinners/`)
        },

        fetchEntreeSideOverall: () => {
            return $http.get(`${apiUrl}/entree/sideoverall/`)
        },


        // Starters
        fetchStarterProteinWinners: () => {
            return $http.get(`${apiUrl}/starter/proteinwinners/`)
        },

        fetchStarterProteinOverall: () => {
            return $http.get(`${apiUrl}/starter/proteinoverall/`)
        },

        fetchStarterSideWinners: () => {
            return $http.get(`${apiUrl}/starter/sidewinners/`)
        },

        fetchStarterSideOverall: () => {
            return $http.get(`${apiUrl}/starter/sideoverall/`)
        },

        fetchStarterProteinStyleWinners: () => {
            return $http.get(`${apiUrl}/starter/proteinstylewinners/`)
        },

        fetchStarterProteinStyleOverall: () => {
            return $http.get(`${apiUrl}/starter/proteinstyleoverall/`)
        },


        // Desserts
        fetchDessertMainWinners: () => {
            return $http.get(`${apiUrl}/dessert/mainwinners/`)
        },

        fetchDessertMainOverall: () => {
            return $http.get(`${apiUrl}/dessert/mainoverall/`)
        },

        fetchDessertSecondaryWinners: () => {
            return $http.get(`${apiUrl}/dessert/secondarywinners/`)
        },

        fetchDessertSecondaryOverall: () => {
            return $http.get(`${apiUrl}/dessert/secondaryoverall/`)
        },

    };

})
