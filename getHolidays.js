let allMonthsHolidays = [];
let daysInMonth = [];
let monthCountDown = 2;

allMonthsHolidays = [];
daysInMonth = [];
monthCountDown = 1;

function handleTr(tr) {
  $(tr).children("td").each(function() {
    let dayNum = $(this).find(".dTS").text();
    if (dayNum.length === 0) return;

    let holidayPortion = 0;
    if ($(this).hasClass("cHD")) holidayPortion = 1;
    if ($(this).hasClass("calendarCpecialDay")) holidayPortion = 0.5;
    let dayText = $(this).find(".cDM").text();
    if (dayText.length <= 1) holidayPortion = 0;

    daysInMonth.push({
      day: dayNum,
      holidayPortion: holidayPortion
    });
  });
}

function collectMonth() {
  if (monthCountDown <= 0) {
    console.log(JSON.stringify(allMonthsHolidays));
    return;
  }

  let monthName = $("#ctl00_mp_calendar_monthChanged").text();

  daysInMonth = [];
  $("#calendar_container").find("tr").each(function() {
    if ($(this).children("td").length === 8) {
      handleTr(this);
    }
  });

  allMonthsHolidays.push({
    monthName: monthName,
    daysInMonth: daysInMonth
  });

  $('#ctl00_mp_calendar_next').click()

  let min = 2, max = 5;
  let rand = Math.floor(Math.random() * (max - min + 1) + min);
  console.log(monthName, 'Counter at', monthCountDown, 'Sleeping for', rand);
  monthCountDown--;
  setTimeout(collectMonth, rand * 1000);
}

collectMonth();
