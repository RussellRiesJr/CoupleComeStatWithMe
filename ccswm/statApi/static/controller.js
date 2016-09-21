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
        return
    };

    $scope.GetWinsByAge = function () {
        StatsFactory.fetchWinsByAge()
        .then((res) => {
            $scope.Title = "Most Wins By Age Group",
            $scope.data1 = res.data
            $location.path('/table')
        })
        return
    };

    $scope.GetWinsByMrtlStat = function () {
        StatsFactory.fetchWinsByMrtlStat()
        .then((res) => {
            $scope.Title = "Most Wins By Marital Status",
            $scope.data1 = res.data
            $location.path('/table')
        })
        return
    };
})

.controller("MainCtrl", function(StatsFactory, $scope) {

})

.controller("NavCtrl", function(StatsFactory, $scope, $location) {
    $scope.go = function () {
        console.log("go executed", $scope.FunctionChange)
        if ($scope.FunctionChange === 'WinsByNight') {
            $scope.$parent.GetWinsByNight()
        }
        if ($scope.FunctionChange === 'WinsByAge') {}
            $scope.$parent.GetWinsByAge()
        }
        if ($scope.FunctionChange === 'WinsByMrtlStat') {}
            $scope.$parent.GetWinsByMrtlStat()
    })



.controller("TableCtrl", function($scope) {

    // $scope.$watch('FunctionChange', function(newValue, oldValue) {
    //     if (newValue == 'WinsByNight') {
    //         GetWinsByNight();
    //     }
    //     if (newValue == 'WinsByAge') {
    //         GetWinsByAge();
    //     }
    // });


    

})
