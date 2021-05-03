function showDate()
{
    let today = new Date();

    alert(`${today.getFullYear()}/${today.getMonth() + 1}/${today.getDate()} ${today.getHours()}:${today.getMinutes()} 出席しました！`);
}