
    function updateShamsiCountdown(endTime) {
        const daysElem = document.getElementById("days");
        const hoursElem = document.getElementById("hours");
        const minutesElem = document.getElementById("minutes");
        const secondsElem = document.getElementById("seconds");

        function calculateCountdown() {
            const now = new Date().getTime();
            const distance = endTime - now;

            if (distance < 0) {
                clearInterval(interval);
                daysElem.textContent = "0";
                hoursElem.textContent = "0";
                minutesElem.textContent = "0";
                secondsElem.textContent = "0";
                return;
            }

            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);

            const shamsiDate = jalaali.toJalaali(new Date(endTime));
            const shamsiDay = shamsiDate.jd;
            const shamsiMonth = shamsiDate.jm;
            const shamsiYear = shamsiDate.jy;

            daysElem.textContent = `${shamsiYear}/${shamsiMonth}/${shamsiDay}`;
            hoursElem.textContent = hours;
            minutesElem.textContent = minutes;
            secondsElem.textContent = seconds;
        }

        const interval = setInterval(calculateCountdown, 1000);
        calculateCountdown(); // Initial call
    }

    // Example usage: Set a future Gregorian date and convert it to Shamsi
    const endTime = new Date().getTime() + 7 * 24 * 60 * 60 * 1000; // 7 days from now
    updateShamsiCountdown(endTime);

