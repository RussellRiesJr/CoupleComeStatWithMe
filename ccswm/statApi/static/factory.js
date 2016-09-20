app.factory('StatsFactory', function($http) {

    let Stats;

    return {

        // Scores
        fetchWinsByNight: () => {
            return $http.get('http://localhost:8000/winsby/night/')
        },

        fetchWinsByAge: () => {
            return $http.get('http://localhost:8000/winsby/age/')
        },

        fetchWinsByMrtlStat: () => {
            return $http.get('http://localhost:8000/winsby/mrtlstat/')
        },

        fetchAvgWinScore: () => {
            return $http.get('http://localhost:8000/scores/avgwin/')
        },

        fetchAvgScoreOverall: () => {
            return $http.get('http://localhost:8000/scores/avgoverall/')
        },

        fetchAvgCoupleVote: () => {
            return $http.get('http://localhost:8000/scores/avgcouple/')
        },

        fetchHighestScore: () => {
            return $http.get('http://localhost:8000/scores/highest/')
        },

        fetchLowestScore: () => {
            return $http.get('http://localhost:8000/scores/lowest/')
        },

        fetchHighestLosingScore: () => {
            return $http.get('http://localhost:8000/scores/highlosing/')
        },

        fetchLowestWinningScore: () => {
            return $http.get('http://localhost:8000/scores/lowwinning/')
        },


        // Entrees
        fetchEntreeProteinWinners: () => {
            return $http.get('http://localhost:8000/entree/proteinwinners/')
        },

        fetchEntreeProteinOverall: () => {
            return $http.get('http://localhost:8000/entree/proteinoverall/')
        },

        fetchEntreeProteinStyleWinners: () => {
            return $http.get('http://localhost:8000/entree/proteinstylewinners/')
        },

        fetchEntreeProteinStyleOverall: () => {
            return $http.get('http://localhost:8000/entree/proteinstyleoverall/')
        },

        fetchEntreeSideWinners: () => {
            return $http.get('http://localhost:8000/entree/sidewinners/')
        },

        fetchEntreeSideOverall: () => {
            return $http.get('http://localhost:8000/entree/sideoverall/')
        },


        // Starters
        fetchStarterProteinWinners: () => {
            return $http.get('http://localhost:8000/starter/proteinwinners/')
        },

        fetchStarterProteinOverall: () => {
            return $http.get('http://localhost:8000/starter/proteinoverall/')
        },

        fetchStarterSideWinners: () => {
            return $http.get('http://localhost:8000/starter/sidewinners/')
        },

        fetchStarterSideOverall: () => {
            return $http.get('http://localhost:8000/starter/sideoverall/')
        },

        fetchStarterProteinStyleWinners: () => {
            return $http.get('http://localhost:8000/starter/proteinstylewinners/')
        },

        fetchStarterProteinStyleOverall: () => {
            return $http.get('http://localhost:8000/starter/proteinstyleoverall/')
        },


        // Desserts
        fetchDessertMainWinners: () => {
            return $http.get('http://localhost:8000/dessert/mainwinners/')
        },

        fetchDessertMainOverall: () => {
            return $http.get('http://localhost:8000/dessert/mainoverall/')
        },

        fetchDessertSecondaryWinners: () => {
            return $http.get('http://localhost:8000/dessert/secondarywinners/')
        },

        fetchDessertSecondaryOverall: () => {
            return $http.get('http://localhost:8000/dessert/secondaryoverall/')
        },

    };

})
