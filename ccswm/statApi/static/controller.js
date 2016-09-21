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

    $scope.GetAvgWinOverall = function () {
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
    }
})


.controller("TableCtrl", function($scope) {

})
