app = angular.module('ccswm', ['ngRoute'])
    .config(($routeProvider) => {
        $routeProvider
            .when('/', {
                controller: 'MainCtrl',
                templateUrl: 'ccswm/statApi/static/partials/home.html'
            })
            .when('/table', {
                controller: 'TableCtrl',
                templateUrl: 'ccswm/statApi/static/partials/tablestat.html'
            })
            .when('/single', {
                controller: 'SingleCtrl',
                templateUrl: 'ccswm/statApi/static/partials/singlestat.html'
            })
            .otherwise('/')
    })


.controller("MasterCtrl", function(StatsFactory, $scope, $location) {
    $scope.data1 = null;
    $scope.Title = "";

    $scope.GetWinsByNight = function () {
        StatsFactory.fetchWinsByNight()
        .then((res) => {
            $scope.Title = "Most Wins By Night",
            $scope.data1 = res.data
            $location.path('/table')
        })
    };

    $scope.GetWinsByAge = function () {
        StatsFactory.fetchWinsByAge()
        .then((res) => {
            $scope.Title = "Most Wins By Age Group",
            $scope.data1 = res.data
            $location.path('/table')
        })
    };

    $scope.GetWinsByMrtlStat = function () {
        StatsFactory.fetchWinsByMrtlStat()
        .then((res) => {
            $scope.Title = "Most Wins By Marital Status",
            $scope.data1 = res.data
            $location.path('/table')
        })
    };

    $scope.GetAvgWinScore = function () {
        StatsFactory.fetchAvgWinScore()
        .then((res) => {
            $scope.Title = "Average Winning Score",
            $scope.data1 = res.data
            $location.path('/single')
        })
    };

    $scope.GetAvgScoreOverall = function () {
        StatsFactory.fetchAvgScoreOverall()
        .then((res) => {
            $scope.Title = "Average Score Overall",
            $scope.data1 = res.data
            $location.path('/single')
        })
    };

    $scope.GetAvgCoupleVote = function () {
        StatsFactory.fetchAvgCoupleVote()
        .then((res) => {
            $scope.Title = "Average Vote By Couple",
            $scope.data1 = res.data
            $location.path('/single')
        })
    };

    $scope.GetHighestScore = function () {
        StatsFactory.fetchHighestScore()
        .then((res) => {
            $scope.Title = "Highest Score",
            $scope.data1 = res.data
            $location.path('/single')
        })
    };

    $scope.GetLowestScore = function () {
        StatsFactory.fetchLowestScore()
        .then((res) => {
            $scope.Title = "Lowest Score",
            $scope.data1 = res.data
            $location.path('/single')
        })
    };

    $scope.GetHighestLosingScore = function () {
        StatsFactory.fetchHighestLosingScore()
        .then((res) => {
            $scope.Title = "Highest Losing Score",
            $scope.data1 = res.data
            $location.path('/single')
        })
    };

    $scope.GetLowestWinningScore = function () {
        StatsFactory.fetchLowestWinningScore()
        .then((res) => {
            $scope.Title = "Lowest Winning Score",
            $scope.data1 = res.data
            $location.path('/single')
        })
    };

    $scope.GetEntreeProteinWinners = function () {
        StatsFactory.fetchEntreeProteinWinners()
        .then((res) => {
            $scope.Title = "Entree Main Ingredient By Winners",
            $scope.data1 = res.data
            $location.path('/table')
        })
    };

    $scope.GetEntreeProteinOverall = function () {
        StatsFactory.fetchEntreeProteinOverall()
        .then((res) => {
            $scope.Title = "Entree Main Ingredient Overall",
            $scope.data1 = res.data
            $location.path('/table')
        })
    };

    $scope.GetEntreeProteinStyleWinners = function () {
        StatsFactory.fetchEntreeProteinStyleWinners()
        .then((res) => {
            $scope.Title = "Entree Main Style By Winners",
            $scope.data1 = res.data
            $location.path('/table')
        })
    };

    $scope.GetEntreeProteinStyleOverall = function () {
        StatsFactory.fetchEntreeProteinStyleOverall()
        .then((res) => {
            $scope.Title = "Entree Main Style Overall",
            $scope.data1 = res.data
            $location.path('/table')
        })
    };

    $scope.GetEntreeSideWinners = function () {
        StatsFactory.fetchEntreeSideWinners()
        .then((res) => {
            $scope.Title = "Entree Side By Winners",
            $scope.data1 = res.data
            $location.path('/table')
        })
    };

    $scope.GetEntreeSideOverall = function () {
        StatsFactory.fetchEntreeSideOverall()
        .then((res) => {
            $scope.Title = "Entree Side Overall",
            $scope.data1 = res.data
            $location.path('/table')
        })
    };

    $scope.GetStarterProteinWinners = function () {
        StatsFactory.fetchStarterProteinWinners()
        .then((res) => {
            $scope.Title = "Starter Main Ingredient By Winners",
            $scope.data1 = res.data
            $location.path('/table')
        })
    };

    $scope.GetStarterProteinOverall = function () {
        StatsFactory.fetchStarterProteinOverall()
        .then((res) => {
            $scope.Title = "Starter Main Ingredient Overall",
            $scope.data1 = res.data
            $location.path('/table')
        })
    };

    $scope.GetStarterProteinStyleWinners = function () {
        StatsFactory.fetchStarterProteinStyleWinners()
        .then((res) => {
            $scope.Title = "Starter Main Style By Winners",
            $scope.data1 = res.data
            $location.path('/table')
        })
    };

    $scope.GetStarterProteinStyleOverall = function () {
        StatsFactory.fetchStarterProteinStyleOverall()
        .then((res) => {
            $scope.Title = "Starter Main Style Overall",
            $scope.data1 = res.data
            $location.path('/table')
        })
    };

    $scope.GetStarterSideWinners = function () {
        StatsFactory.fetchStarterSideWinners()
        .then((res) => {
            $scope.Title = "Starter Side By Winners",
            $scope.data1 = res.data
            $location.path('/table')
        })
    };

    $scope.GetStarterSideOverall = function () {
        StatsFactory.fetchStarterSideOverall()
        .then((res) => {
            $scope.Title = "Starter Side Overall",
            $scope.data1 = res.data
            $location.path('/table')
        })
    };

    $scope.GetDessertMainWinners = function () {
        StatsFactory.fetchDessertMainWinners()
        .then((res) => {
            $scope.Title = "Dessert Main Ingredient By Winners",
            $scope.data1 = res.data
            $location.path('/table')
        })
    };

    $scope.GetDessertMainOverall = function () {
        StatsFactory.fetchDessertMainOverall()
        .then((res) => {
            $scope.Title = "Dessert Main Ingredient Overall",
            $scope.data1 = res.data
            $location.path('/table')
        })
    };

    $scope.GetDessertSecondaryWinners = function () {
        StatsFactory.fetchDessertSecondaryWinners()
        .then((res) => {
            $scope.Title = "Dessert Side Ingredient By Winners",
            $scope.data1 = res.data
            $location.path('/table')
        })
    };

    $scope.GetDessertSecondaryOverall = function () {
        StatsFactory.fetchDessertSecondaryOverall()
        .then((res) => {
            $scope.Title = "Dessert Side Ingredient Overall",
            $scope.data1 = res.data
            $location.path('/table')
        })
    };
})

.controller("MainCtrl", function(StatsFactory, $scope) {

})

.controller("NavCtrl", function(StatsFactory, $scope, $location) {
    $scope.go = function () {
        console.log("go executed", $scope.FunctionChange)
        if ($scope.FunctionChange === 'WinsByNight') {
            $scope.$parent.GetWinsByNight()
            return
        }
        if ($scope.FunctionChange === 'WinsByAge') {
            $scope.$parent.GetWinsByAge()
            return
        }
        if ($scope.FunctionChange === 'WinsByMrtlStat') {
            $scope.$parent.GetWinsByMrtlStat()
            return
        }
        if ($scope.FunctionChange === 'AvgWinScore') {
            $scope.$parent.GetAvgWinScore()
            return
        }
        if ($scope.FunctionChange === 'AvgScoreOverall') {
            $scope.$parent.GetAvgScoreOverall()
            return
        }
        if ($scope.FunctionChange === 'AvgCoupleVote') {
            $scope.$parent.GetAvgCoupleVote()
            return
        }
        if ($scope.FunctionChange === 'HighestScore') {
            $scope.$parent.GetHighestScore()
            return
        }
        if ($scope.FunctionChange === 'LowestScore') {
            $scope.$parent.GetLowestScore()
            return
        }
        if ($scope.FunctionChange === 'HighestLosingScore') {
            $scope.$parent.GetHighestLosingScore()
            return
        }
        if ($scope.FunctionChange === 'LowestWinningScore') {
            $scope.$parent.GetLowestWinningScore()
            return
        }
        if ($scope.FunctionChange === 'EntreeProteinWinners') {
            $scope.$parent.GetEntreeProteinWinners()
            return
        }
        if ($scope.FunctionChange === 'EntreeProteinOverall') {
            $scope.$parent.GetEntreeProteinOverall()
            return
        }
        if ($scope.FunctionChange === 'EntreeProteinStyleWinners') {
            $scope.$parent.GetEntreeProteinStyleWinners()
            return
        }
        if ($scope.FunctionChange === 'EntreeProteinStyleOverall') {
            $scope.$parent.GetEntreeProteinStyleOverall()
            return
        }
        if ($scope.FunctionChange === 'EntreeSideWinners') {
            $scope.$parent.GetEntreeSideWinners()
            return
        }
        if ($scope.FunctionChange === 'EntreeSideOverall') {
            $scope.$parent.GetEntreeSideOverall()
            return
        }
        if ($scope.FunctionChange === 'StarterProteinWinners') {
            $scope.$parent.GetStarterProteinWinners()
            return
        }
        if ($scope.FunctionChange === 'StarterProteinOverall') {
            $scope.$parent.GetStarterProteinOverall()
            return
        }
        if ($scope.FunctionChange === 'StarterProteinStyleWinners') {
            $scope.$parent.GetStarterProteinStyleWinners()
            return
        }
        if ($scope.FunctionChange === 'StarterProteinStyleOverall') {
            $scope.$parent.GetStarterProteinStyleOverall()
            return
        }
        if ($scope.FunctionChange === 'StarterSideWinners') {
            $scope.$parent.GetStarterSideWinners()
            return
        }
        if ($scope.FunctionChange === 'StarterSideOverall') {
            $scope.$parent.GetStarterSideOverall()
            return
        }
        if ($scope.FunctionChange === 'DessertMainWinners') {
            $scope.$parent.GetDessertMainWinners()
            return
        }
        if ($scope.FunctionChange === 'DessertMainOverall') {
            $scope.$parent.GetDessertMainOverall()
            return
        }
        if ($scope.FunctionChange === 'DessertSecondaryWinners') {
            $scope.$parent.GetDessertSecondaryWinners()
            return
        }
        if ($scope.FunctionChange === 'DessertSecondaryOverall') {
            $scope.$parent.GetDessertSecondaryOverall()
            return
        }
    }
})


.controller("TableCtrl", function($scope) {

})

.controller("SingleCtrl", function($scope) {

})
