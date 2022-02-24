// LOAD DATA
$(document).ready(function(){

    $.post('/API/dashboard', {}, 
        function(data, status, xhr) {
            
            $("#ref_session_data").html(data.data.session_data)

            $("#ref_last_session_score").html(data.data.last_session_score)
            $("#ref_last_session_total").html(data.data.last_session_total)

            corrected_percent = parseFloat(data.data.last_session_percent).toFixed(2)
            $("#ref_last_session_percent").html(corrected_percent)

            $("#ref_session_tot_percent_5").html(parseFloat(data.data.session_tot_percent_5).toFixed(2))
            $("#ref_session_tot_percent_10").html(parseFloat(data.data.session_tot_percent_10).toFixed(2))
            $("#ref_session_tot_percent_20").html(parseFloat(data.data.session_tot_percent_20).toFixed(2))
            $("#ref_session_tot_percent_30").html(parseFloat(data.data.session_tot_percent_30).toFixed(2))

            //////////////////////////////////////////////////////////////////////////////
            // PERCENTAGE CHART
            const ctx_percentage = document.getElementById('percentage_chart').getContext('2d');
            const percentageChart = new Chart(ctx_percentage, {
                type: 'bar',
                data: {
                    labels: ['1','2','3','4','5','6','7','8','9','10'],
                    datasets: [{
                        label: '10 days percentage',
                        data: data.data.session_percentage_10,
                        backgroundColor: [
                            'rgba(54, 162, 235, 0.2)'
                        ],
                        borderColor: [
                            'rgba(54, 162, 235, 0.2)'
                        ],
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });

            //////////////////////////////////////////////////////////////////////////////
            // ERRORS CHART
            const ctx_errors = document.getElementById('errors_chart').getContext('2d');
            const errorsChart = new Chart(ctx_errors, {
                type: 'bar',
                data: {
                    labels: ['1','2','3','4','5','6','7','8','9','10'],
                    datasets: [{
                        label: '10 days errors',
                        data: data.data.errors_10,
                        backgroundColor: [
                            'rgba(255, 99, 132, 0.2)'
                        ],
                        borderColor: [
                            'rgba(255, 99, 132, 0.2)'
                        ],
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });

            //////////////////////////////////////////////////////////////////////////////
            // SCORE CHART
            const ctx_score = document.getElementById('score_chart').getContext('2d');
            const scoreChart = new Chart(ctx_score, {
                type: 'bar',
                data: {
                    labels: ['1','2','3','4','5','6','7','8','9','10'],
                    datasets: [{
                        label: '10 days scores',
                        data: data.data.scored_point_10,
                        backgroundColor: [
                            'rgba(255, 206, 86, 0.2)'
                        ],
                        borderColor: [
                            'rgba(255, 206, 86, 1)'
                        ],
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });

            //////////////////////////////////////////////////////////////////////////////
            // SHOTS CHART
            const ctx_shots = document.getElementById('shots_chart').getContext('2d');
            const shotsChart = new Chart(ctx_shots, {
                type: 'bar',
                data: {
                    labels: ['1','2','3','4','5','6','7','8','9','10'],
                    datasets: [{
                        label: '10 days shots',
                        data: data.data.shooted_points_10,
                        backgroundColor: [
                            'rgba(75, 192, 192, 0.2)'
                        ],
                        borderColor: [
                            'rgba(75, 192, 192, 1)'
                        ],
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });

            //console.log(data)
        })

        .fail(function(jqxhr, settings, ex) { 
            alert(LOADING_ERROR + ex); 
        });

});

