exports.picker = function(prices) {
    let biggestSpread = 0
    let buySell = []
    for (day= 0; day, day < prices.length; day++) {   
        let sum = 0;
        for(let i =day+1 ; i < prices.length; i++){ 
            sum = (prices[i] - prices[day])
            if (sum > biggestSpread) {
                biggestSpread = sum;
                buySell[0] = day;
                buySell[1] = i;
            }
        }
    }
    return buySell
}
