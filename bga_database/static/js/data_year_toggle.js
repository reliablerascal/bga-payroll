function initDataYearToggle (endpoint, slug, initialYear, callback) {
    var getData = async function (year) {
        var url;

        if ( slug === null ) {
            url = `/${endpoint}/?data_year=${year}`;
        } else {
            url = `/${endpoint}/${slug}/?data_year=${year}`;
        }

        try {
            const result = await $.ajax({
                url: url,
                type: 'GET',
            });
            callback(year, result);
            $('#yearDropdownMenuButton').text(year);
        } catch (error) {
            console.error(error);
        }

        return;
    };

    getData(initialYear);

    $('#data-year-select > .year-dropdown-item').on('click', function(e) {
        const year = e.currentTarget.textContent;
        getData(year);
    });
}

export { initDataYearToggle };
