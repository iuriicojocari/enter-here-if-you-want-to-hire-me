from bs4 import BeautifulSoup
import collections

ALLOWED_TITLE = set(['Suits'])
data = '''

<!DOCTYPE html><html><head>
<title>TorrentsMd - BitTorrent Tracker Moldova</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta name="referrer" content="always">
<link rel="search" type="application/opensearchdescription+xml" title="Căutare pe torrentsmd.eu" href="http://torrentsmd.eu/opensearch.xml">
<link rel="stylesheet" href="/cache/packed.css?v=89" type="text/css"/>
<link rel="stylesheet" href="/styles/main.css" type="text/css"/>
<script type="text/javascript" src="https://gc.kis.v2.scr.kaspersky-labs.com/26A5EC9C-E127-C042-B7D4-EC8444565209/main.js" charset="UTF-8"></script><script type="text/javascript" src="/cache/packed.js?v=64"></script>
<link rel="canonical" href="https://www.torrentsmd.com/browse.php" />
<link rel="icon"  href="/pic/favicon.png" type="image/png" />
</head>
<body>
<script>
var logo = 'torrents_logo.png',logo_width = '280',logo_main_title= '', logo_map_title = '',logo_map = '',logo_map_link= '';
message.lang = 'ro';
cap_login = false;

var custom_html_to_menu = '<img height=49 src="/pic/meniu_separator.gif" width=16 align=absMiddle><a href="https://topicmd.com/wall/news.php"><span style="color:#d6a5ff">(topicmd.com)</span> Noutățile prietenilor</a>';
</script>
<style type="text/css">.lang-ru-hide-all, .lang-ru-hide { display:none; visibility: hidden;}</style> <!-- special lang bbcode --><img style="display:none" src="/pic/transparency.gif">
<div id="overlay"></div>
<div id="navbar_login_menu" class="zburator_invizibil">
<form method="post" name="login_form" action="takelogin.php" onsubmit="return startLoginVerify();">
  <table id="login_form" border="0" cellpadding=5>
  <tr>
    <td colspan="2" align="right">
      <img style="cursor:pointer;" onClick="close_login_box();" src="/pic/close.gif" align="right">
    </td>
  </tr>
  <tr>
    <td class=rowhead style="padding-left:25px;">User:</td>
    <td align=left style="padding-right:25px;">
      <input type="text" size=30 name="username" id="navbar_login_menu_input_to_focus_on" />
    </td>
  </tr>
  <tr>
    <td class=rowhead>Parola:</td>
    <td align=left><input type="password" size=30 name="password" /></td>
  </tr>
  <tr>
    <td colspan=2 align="left" style="border-bottom:0px;">
      <input type="checkbox" name="autologin" id="autologin" value="1" checked="checked" />
        <label for="autologin">Autentificare automată la următoarea vizită</label>
    </td>
  </tr>
  <tr>
    <td colspan=2 align="center" style="border-top:0px;">
      <input type="submit" value="  Intră  " class="but_blue" style="font-weight: bold;padding: 4px;">
      <div id="login_status">&nbsp;</div>
    </td>
  </tr>
  <tr>
    <td colspan=2 align="center">
      <a href="signup.php">Înregistrare</a> |
      <a href="recover.php">Restabilirea parolei</a> |
      <br/>
      <a href="confirm_no_email.php">Scrisoarea cu confirmare nu a venit</a>
    </td>
  </tr>
  </table>
</form>
</div>
<div id="no_td_border">
<!-- For those who have JS disabled-->
<noscript><iframe src="/lang/noscript_top_and_menu.html" width="100%" height="125" scrolling="no" frameborder="0"></iframe></noscript>
<noscript><style type="text/css">.sp-body { display:block; }</style></noscript>
<div id="top_menu"></div><!-- Top Menu Writed By JS -->
<div id="main_menu"></div><!-- Main Menu Writed By JS -->

<div align="right">
<script type="text/javascript">
// Lang switcher
lang = readCookie('lang');
if (!lang || lang == 'ro') document.write('<a style="cursor:pointer;" onclick="createCookie(\'lang\',\'ru\');location.reload();"><b>RU</b></a> | RO&nbsp;');
else document.write('RU | <a style="cursor:pointer;" onclick="createCookie(\'lang\',\'ro\');location.reload();"><b>RO</b></a>&nbsp;');
</script>
</div>
<script type="text/javascript">ShowMenu(1);</script><script type="text/javascript" src="/js/login.js?v=7"></script></div> <!--End Of no_td_border-->
<div class="pageContainer"  >

<br/><div align="left" style="width:780px;"><a href="/browse_filters.php" id="browseAdvFilterLink">Filtrare avansată</a> | <a class="rss" href="/rss.php?key=LGViMmFmOGE5ZDYxZDI5Y2ViODg4NTQ0NDdjZThiOTQyZmZhNmRkNTliMDM5YWI4ZjA3MjM2NzlhNjExOWNkMGE">RSS</a> (<a href="/forum.php?action=viewtopic&topicid=88143103">?</a>)</div><br>
<script language="JavaScript" src="./js/browse.js" type="text/javascript"></script>

<div class="mCenter categories">
    <div class="tipContinut">
        <a href="./browse.php?categtags=89&amp;not_categtags=45">Filme</a>
        <a href="./browse.php?categtags=90">Muzică</a>
        <a href="./browse.php?categtags=92">Software</a>
        <a href="./browse.php?categtags=93">Jocuri</a>
        <a href="./browse.php?categtags=94">Emisiuni TV</a>
        <a href="./browse.php?categtags=95">Cărţi</a>
        <a href="./browse.php?categtags=96">Muzică video</a>
        <a href="./browse.php?categtags=97">Anime</a>
        <a href="./browse.php?categtags=98">Filme animate</a>
        <a href="./browse.php?categtags=99">Cărți audio</a>
        <a href="./browse.php?categtags=100">Lecţii video</a>
        <a href="./browse.php?categtags=101">Fotografii</a>
        <a href="./browse.php?categtags=312">Altceva</a>
        <a href="./browse.php?categtags=313">Documentare</a>
        <a href="./browse.php?categtags=314">Sport</a>
        <a href="./browse.php?cat=12" style="color:#707607;">DVD</a>
        <a href="./browse.php?cat=18" style="color:#707607;">HDTV</a>
        <a href="./browse.php?categtags=45" style="color: green; text-decoration:underline">Seriale</a>
    </div>

<!--</div>-->

</td></tr></table>
<br/>
<div class="categFatherName">Limbi</div><br />
<div class="tipContinut">
            <a href="/browse.php?categtags=27#torrents">Română</a><a href="/browse.php?categtags=28#torrents">Rusă</a><a href="/browse.php?categtags=180#torrents">Engleză</a><a href="/browse.php?categtags=185#torrents">Italiană</a><a href="/browse.php?categtags=182#torrents">Franceză</a><a href="/browse.php?categtags=183#torrents">Spaniolă</a><a href="/browse.php?categtags=181#torrents">Germană</a><a href="/browse.php?categtags=184#torrents">Japoneză</a><a href="/browse.php?categtags=315#torrents">Ucraineană</a><a href="/browse.php?categtags=316#torrents">Hindi</a></div>
</div>  <!--de sters cand uitam de ?cat -->
<script type="text/javascript">topVerGen=1505488623;
        print_browse_top_menu();</script>
<h2 id="torrents_header"></h2>
<div class="center browseHeader" id="torrents">
<h2>Ultimele torrente</h2><p><a href="/top_imdb.php"><b>Top filme recente IMDB</b></a> | <a href="/top_by_category.php"><b>Top pentru fiecare categorie</b></a> | <a href="/forum.php?action=viewtopic&topicid=87944758" target="_blank">IMDb Top 250</a></p>Primele 5 - cele mai populare torrente din ultimele 24 ore
    <div align="center" style="padding-top: 4px;padding-bottom: 7px;"><b>&lt;&lt;&nbsp;Precedenta</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="browse.php?page=1"><b>Următoarea&nbsp;&gt;&gt;</b></a><br /><b>1&nbsp;-&nbsp;100</b> | <a href="browse.php?page=1"><b>101&nbsp;-&nbsp;200</b></a> | <a href="browse.php?page=2"><b>201&nbsp;-&nbsp;300</b></a> | ... | <a href="browse.php?page=5146"><b>514601&nbsp;-&nbsp;514700</b></a> | <a href="browse.php?page=5147"><b>514701&nbsp;-&nbsp;514800</b></a> | <a href="browse.php?page=5148"><b>514801&nbsp;-&nbsp;514863</b></a></div>
<style>td.colhead a {color: #ffffff;text-decoration: underline;}
.tableTorrents a {
    font-weight: bold;
}
</style>
        <table border="1" cellspacing=0 cellpadding=5 width="990" class="tableTorrents">

        <colgroup>
        	<col width="42"></col>
			<col></col>
			<col></col>
			<col></col>
			<col></col>
			<col></col>
			<col></col>
			<col></col>
			<col></col>
			<col></col>
        </colgroup>

        <tr>
          <td class="colhead" align="center">Tip</td>
          <td class="colhead" align="left">Nume</td>
          <td class="colhead" align="right">Fiş.</td>
          <td class="colhead" align="right">Com.</td>
                    <td class="colhead" align="center">Adăugat</td>
                    <td class="colhead" align="center">Mărime</td>
                    <td class="colhead" align="right"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/arrowup.gif"></td>
                     <td class="colhead" align="right"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/arrowdown.gif"></td>
          <td class="colhead" align="right">Mulț.</td>
          <td class="colhead" align="center" style="white-space: nowrap;">Încărcat de</td>
          </tr>
<tr style="background-color: #F2DCDC;">
<td class="torrentCategImg"><a href="browse.php?cat=1"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_movie.gif" height="32" alt="Movies"/></a></td>
<td align=left><a href="/details.php?id=1518422">Бабушка лёгкого поведения [2017 / WEB-DL] [Comedy]</a>
</td>
<td align="right">1</td>
<td align="right"><a href="details.php?id=1518422&amp;page=0#startcomments">6</a></td>
<td align=center width=20><nobr>21 ore</nobr></td>
<td align=center><nobr>1.37 GB</nobr></td>
<td align=right><a href=details.php?id=1518422&amp;toseeders=1><font color=#000000>589</font></a></td>
<td align=right><a href=details.php?id=1518422&amp;todlers=1>61</a></td>
<td align="right">83</td><td align=center nowrap><a href=userdetails.php?id=32199>V!ad</a></td>
</tr>
<tr style="background-color: #F2DCDC;">
<td class="torrentCategImg"><a href="browse.php?cat=1"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_movie.gif" height="32" alt="Movies"/></a></td>
<td align=left><a href="browse.php?imdb=3890160">Baby Driver / Малыш на драйве [2017 / WEB-DL] [Action / Crime / Thriller] [8.1/10]</a>
</td>
<td align="right">1</td>
<td align="right"><a href="details.php?id=1518418&amp;page=0#startcomments">7</a></td>
<td align=center width=20><nobr>22 ore</nobr></td>
<td align=center><nobr>1.46 GB</nobr></td>
<td align=right><a href=details.php?id=1518418&amp;toseeders=1><font color=#000000>390</font></a></td>
<td align=right><a href=details.php?id=1518418&amp;todlers=1>51</a></td>
<td align="right">46</td><td align=center nowrap><a href=userdetails.php?id=136958>anronn</a></td>
</tr>
<tr style="background-color: #F2DCDC;">
<td class="torrentCategImg"><a href="browse.php?cat=18"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_hdtv.gif" height="29" alt="HDTV"/></a></td>
<td align=left><a href="browse.php?imdb=3371366" style="color:#707607">Transformers: The Last Knight / Трансформеры: Последний рыцарь [2017 / BDRip 1080p] [Action / Adventure / Sci-Fi] [5.3/10]</a>
</td>
<td align="right">1</td>
<td align="right"><a href="details.php?id=1518417&amp;page=0#startcomments">2</a></td>
<td align=center width=20><nobr>23 ore</nobr></td>
<td align=center><nobr>17.31 GB</nobr></td>
<td align=right><a href=details.php?id=1518417&amp;toseeders=1><font color=#000000>115</font></a></td>
<td align=right><a href=details.php?id=1518417&amp;todlers=1>39</a></td>
<td align="right">27</td><td align=center nowrap><a href=userdetails.php?id=32199>V!ad</a></td>
</tr>
<tr style="background-color: #F2DCDC;">
<td class="torrentCategImg"><a href="browse.php?cat=1"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_movie.gif" height="32" alt="Movies"/></a></td>
<td align=left><a href="browse.php?imdb=6944936">Party Boat / Вечеринка на яхте [2017 / WEB-DL] [Comedy]</a>
</td>
<td align="right">1</td>
<td align="right"><a href="details.php?id=1518419&amp;page=0#startcomments">2</a></td>
<td align=center width=20><nobr>22 ore</nobr></td>
<td align=center><nobr>1.37 GB</nobr></td>
<td align=right><a href=details.php?id=1518419&amp;toseeders=1><font color=#000000>94</font></a></td>
<td align=right><a href=details.php?id=1518419&amp;todlers=1>9</a></td>
<td align="right">16</td><td align=center nowrap><a href=userdetails.php?id=136958>anronn</a></td>
</tr>
<tr style="background-color: #F2DCDC;">
<td class="torrentCategImg"><a href="browse.php?cat=18"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_hdtv.gif" height="29" alt="HDTV"/></a></td>
<td align=left><a href="/details.php?id=1518423" style="color:#707607">Бабушка лёгкого поведения [1080p] [2017 / WEB-DL] [Comedy]</a>
</td>
<td align="right">1</td>
<td align="right">0</td>
<td align=center width=20><nobr>21 ore</nobr></td>
<td align=center><nobr>3.14 GB</nobr></td>
<td align=right><a href=details.php?id=1518423&amp;toseeders=1><font color=#000000>41</font></a></td>
<td align=right><a href=details.php?id=1518423&amp;todlers=1>4</a></td>
<td align="right">9</td><td align=center nowrap><a href=userdetails.php?id=32199>V!ad</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=2"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_music.gif" height="32" alt="Music"/></a></td>
<td align=left><a href="/details.php?id=1518441">VA - Boom Hits Vol.769 - 2017 [2017 / MP3 / 320] [Dance]</a>
</td>
<td align="right"><a href="details.php?id=1518441&amp;filelist=1">42</a></td>
<td align="right"><a href="details.php?id=1518441&amp;page=0#startcomments">1</a></td>
<td align=center width=20><nobr>22 minute</nobr></td>
<td align=center><nobr>310.34 MB</nobr></td>
<td align="right"><span class="red">0</span></td>
<td align=right><a href=details.php?id=1518441&amp;todlers=1>7</a></td>
<td align="right">2</td><td align=center nowrap><a href=userdetails.php?id=777705>masterdj2011</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=5"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_tv.gif" height="32" alt="TV"/></a></td>
<td align=left><a href="/details.php?id=1518442">Lethal Weapon / Смертельное оружие [ColdFilm] [Season 2/Episode 1] [2017 / WEB-DL] [8.1/10]</a>
</td>
<td align="right">1</td>
<td align="right"><a href="details.php?id=1518442&amp;page=0#startcomments">1</a></td>
<td align=center width=20><nobr>44 minute</nobr></td>
<td align=center><nobr>399.24 MB</nobr></td>
<td align=right><a href=details.php?id=1518442&amp;toseeders=1><font color=#000000>13</font></a></td>
<td align=right><a href=details.php?id=1518442&amp;todlers=1>2</a></td>
<td align="right">3</td><td align=center nowrap><a href=userdetails.php?id=787439>Good_Like</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=5"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_tv.gif" height="32" alt="TV"/></a></td>
<td align=left><a href="/details.php?id=1518440">Открытый микрофон [Season 2/Episode 5] [2017 / SATRip]</a>
</td>
<td align="right">1</td>
<td align="right">0</td>
<td align=center width=20><nobr>1 ore</nobr></td>
<td align=center><nobr>635.94 MB</nobr></td>
<td align=right><a href=details.php?id=1518440&amp;toseeders=1><font color=#000000>106</font></a></td>
<td align=right><a href=details.php?id=1518440&amp;todlers=1>18</a></td>
<td align="right">5</td><td align=center nowrap><a href=userdetails.php?id=136958>anronn</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=1"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_movie.gif" height="32" alt="Movies"/></a></td>
<td align=left><a href="/details.php?id=1518439">Семейные радости Анны [2017 / SATRip] [Comedy / Romance]</a>
</td>
<td align="right">1</td>
<td align="right">0</td>
<td align=center width=20><nobr>2 ore</nobr></td>
<td align=center><nobr>1.37 GB</nobr></td>
<td align=right><a href=details.php?id=1518439&amp;toseeders=1><font color=#000000>11</font></a></td>
<td align=right><a href=details.php?id=1518439&amp;todlers=1>4</a></td>
<td align="right">2</td><td align=center nowrap><a href=userdetails.php?id=136958>anronn</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=5"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_tv.gif" height="32" alt="TV"/></a></td>
<td align=left><a href="/details.php?id=1518437">Love Is [Episode 5] [2017 / SATRip]</a>
</td>
<td align="right">1</td>
<td align="right">0</td>
<td align=center width=20><nobr>2 ore</nobr></td>
<td align=center><nobr>315.82 MB</nobr></td>
<td align=right><a href=details.php?id=1518437&amp;toseeders=1><font color=#000000>47</font></a></td>
<td align=right><a href=details.php?id=1518437&amp;todlers=1>3</a></td>
<td align="right">1</td><td align=center nowrap><a href=userdetails.php?id=136958>anronn</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=5"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_tv.gif" height="32" alt="TV"/></a></td>
<td align=left><a href="/details.php?id=1518436">Голос [Season 6/Episode 3] [2016 / SATRip]</a>
</td>
<td align="right">1</td>
<td align="right"><a href="details.php?id=1518436&amp;page=0#startcomments">1</a></td>
<td align=center width=20><nobr>3 ore</nobr></td>
<td align=center><nobr>1.27 GB</nobr></td>
<td align=right><a href=details.php?id=1518436&amp;toseeders=1><font color=#000000>111</font></a></td>
<td align=right><a href=details.php?id=1518436&amp;todlers=1>17</a></td>
<td align="right">12</td><td align=center nowrap><a href=userdetails.php?id=32199>V!ad</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=5"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_tv.gif" height="32" alt="TV"/></a></td>
<td align=left><a href="/details.php?id=1518435">Новый Comedy Club в Барвихе [Episode 235] [2017 / SATRip]</a>
</td>
<td align="right">1</td>
<td align="right"><a href="details.php?id=1518435&amp;page=0#startcomments">1</a></td>
<td align=center width=20><nobr>4 ore</nobr></td>
<td align=center><nobr>606.63 MB</nobr></td>
<td align=right><a href=details.php?id=1518435&amp;toseeders=1><font color=#000000>447</font></a></td>
<td align=right><a href=details.php?id=1518435&amp;todlers=1>27</a></td>
<td align="right">37</td><td align=center nowrap><a href=userdetails.php?id=32199>V!ad</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=2"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_music.gif" height="32" alt="Music"/></a></td>
<td align=left><a href="/details.php?id=1518434">VA - Ibiza Closing Party 2017 - Armada Music [2017 / MP3 / 320] [Dance]</a>
</td>
<td align="right"><a href="details.php?id=1518434&amp;filelist=1">41</a></td>
<td align="right">0</td>
<td align=center width=20><nobr>7 ore</nobr></td>
<td align=center><nobr>313.53 MB</nobr></td>
<td align=right><a href=details.php?id=1518434&amp;toseeders=1><font color=#000000>19</font></a></td>
<td align=right><a href=details.php?id=1518434&amp;todlers=1>2</a></td>
<td align="right">11</td><td align=center nowrap><a href=userdetails.php?id=710443>itsf8</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=17"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_sport.gif" height="32" alt="Sport"/></a></td>
<td align=left><a href="/details.php?id=1518433">WWE Smackdown Live (Русская версия от 545TV) [12.09] [2017 / HDTVRip] [Wrestling]</a>
</td>
<td align="right">1</td>
<td align="right">0</td>
<td align=center width=20><nobr>8 ore</nobr></td>
<td align=center><nobr>882.05 MB</nobr></td>
<td align=right><a href=details.php?id=1518433&amp;toseeders=1><font color=#000000>5</font></a></td>
<td align="right">0</td>
<td align="right">2</td><td align=center nowrap><a href=userdetails.php?id=520915>cprofire</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=17"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_sport.gif" height="32" alt="Sport"/></a></td>
<td align=left><a href="/details.php?id=1518432">WWE Monday Night RAW (Русская версия от 545TV) [11/09] [2017 / HDTVRip] [Wrestling]</a>
</td>
<td align="right">1</td>
<td align="right"><a href="details.php?id=1518432&amp;page=0#startcomments">1</a></td>
<td align=center width=20><nobr>8 ore</nobr></td>
<td align=center><nobr>1.35 GB</nobr></td>
<td align=right><a href=details.php?id=1518432&amp;toseeders=1><font color=#000000>6</font></a></td>
<td align=right><a href=details.php?id=1518432&amp;todlers=1>2</a></td>
<td align="right">2</td><td align=center nowrap><a href=userdetails.php?id=520915>cprofire</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=5"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_tv.gif" height="32" alt="TV"/></a></td>
<td align=left><a href="/details.php?id=1518431">Постскриптум с Алексеем Пушковым [09/09] [2017 / SATRip]</a>
</td>
<td align="right">1</td>
<td align="right">0</td>
<td align=center width=20><nobr>9 ore</nobr></td>
<td align=center><nobr>637.75 MB</nobr></td>
<td align=right><a href=details.php?id=1518431&amp;toseeders=1><font color=#000000>14</font></a></td>
<td align=right><a href=details.php?id=1518431&amp;todlers=1>2</a></td>
<td align="right">2</td><td align=center nowrap><a href=userdetails.php?id=737>megamax</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=17"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_sport.gif" height="32" alt="Sport"/></a></td>
<td align=left><a href="/details.php?id=1518430">Лига Европы 2017-18. 1-й тур. Обзор / Футбол 1 HD [2017 / HDTVRip] [Soccer] [EN]</a>
</td>
<td align="right">1</td>
<td align="right">0</td>
<td align=center width=20><nobr>10 ore</nobr></td>
<td align=center><nobr>1.70 GB</nobr></td>
<td align=right><a href=details.php?id=1518430&amp;toseeders=1><font color=#000000>32</font></a></td>
<td align=right><a href=details.php?id=1518430&amp;todlers=1>2</a></td>
<td align="right">5</td><td align=center nowrap><a href="./team.php?name=Millennium_Releasers_Group">MRG</a> / <a href=userdetails.php?id=6745>Малыш</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=4"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_games.gif" height="32" alt="Games"/></a></td>
<td align=left><a href="/details.php?id=1518426">Divinity: Original Sin 2  [2017 / English] [Role-Playing(RPG)] [EN]</a>
</td>
<td align="right"><a href="details.php?id=1518426&amp;filelist=1">2</a></td>
<td align="right"><a href="details.php?id=1518426&amp;page=0#startcomments">10</a></td>
<td align=center width=20><nobr>16 ore</nobr></td>
<td align=center><nobr>23.53 GB</nobr></td>
<td align=right><a href=details.php?id=1518426&amp;toseeders=1><font color=#000000>5</font></a></td>
<td align=right><a href=details.php?id=1518426&amp;todlers=1>5</a></td>
<td align="right">9</td><td align=center nowrap><a href=userdetails.php?id=303559>Provadimash</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=18"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_hdtv.gif" height="29" alt="HDTV"/></a></td>
<td align=left><a href="/details.php?id=1518429" style="color:#707607">Молодёжка[720] [Season 5 / Episode 11] [2017 / WEB-DL] [Drama / Sport] [5.4/10]</a>
</td>
<td align="right">1</td>
<td align="right">0</td>
<td align=center width=20><nobr>16 ore</nobr></td>
<td align=center><nobr>1.22 GB</nobr></td>
<td align=right><a href=details.php?id=1518429&amp;toseeders=1><font color=#000000>24</font></a></td>
<td align=right><a href=details.php?id=1518429&amp;todlers=1>2</a></td>
<td align="right">4</td><td align=center nowrap><a href="./team.php?name=Millennium_Releasers_Group">MRG</a> / <a href=userdetails.php?id=671739>Parliament10</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=5"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_tv.gif" height="32" alt="TV"/></a></td>
<td align=left><a href="/details.php?id=1518428">Молодёжка [Season 5/Episode 11] [2017 / WEB-DL] [5.4/10]</a>
</td>
<td align="right">1</td>
<td align="right"><a href="details.php?id=1518428&amp;page=0#startcomments">1</a></td>
<td align=center width=20><nobr>17 ore</nobr></td>
<td align=center><nobr>599.73 MB</nobr></td>
<td align=right><a href=details.php?id=1518428&amp;toseeders=1><font color=#000000>204</font></a></td>
<td align=right><a href=details.php?id=1518428&amp;todlers=1>9</a></td>
<td align="right">9</td><td align=center nowrap><a href="./team.php?name=Millennium_Releasers_Group">MRG</a> / <a href=userdetails.php?id=671739>Parliament10</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=2"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_music.gif" height="32" alt="Music"/></a></td>
<td align=left><a href="/details.php?id=1518427">Armin van Buuren - A State of Trance 831 [2017 / MP3 / 320] [Trance]</a>
</td>
<td align="right">1</td>
<td align="right">0</td>
<td align=center width=20><nobr>19 ore</nobr></td>
<td align=center><nobr>272.77 MB</nobr></td>
<td align="right"><span class="red">0</span></td>
<td align=right><a href=details.php?id=1518427&amp;todlers=1>6</a></td>
<td align="right">3</td><td align=center nowrap><a href=userdetails.php?id=474877>4empion</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=18"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_hdtv.gif" height="29" alt="HDTV"/></a></td>
<td align=left><a href="/details.php?id=1518425" style="color:#707607">Бабушка лёгкого поведения [720p] [2017 / WEB-DL] [Comedy]</a>
</td>
<td align="right">1</td>
<td align="right">0</td>
<td align=center width=20><nobr>20 ore</nobr></td>
<td align=center><nobr>2.50 GB</nobr></td>
<td align=right><a href=details.php?id=1518425&amp;toseeders=1><font color=#000000>38</font></a></td>
<td align=right><a href=details.php?id=1518425&amp;todlers=1>2</a></td>
<td align="right">9</td><td align=center nowrap><a href=userdetails.php?id=32199>V!ad</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=18"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_hdtv.gif" height="29" alt="HDTV"/></a></td>
<td align=left><a href="/details.php?id=1518424" style="color:#707607">X Factor România [720p] [Season 7 / Episode 1] [2017 / WEB-DL] [Music] [RO]</a>
</td>
<td align="right">1</td>
<td align="right"><a href="details.php?id=1518424&amp;page=0#startcomments">2</a></td>
<td align=center width=20><nobr>21 ore</nobr></td>
<td align=center><nobr>1.49 GB</nobr></td>
<td align=right><a href=details.php?id=1518424&amp;toseeders=1><font color=#000000>28</font></a></td>
<td align=right><a href=details.php?id=1518424&amp;todlers=1>2</a></td>
<td align="right">14</td><td align=center nowrap><a href=userdetails.php?id=441089>Nonconformist</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=5"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_tv.gif" height="32" alt="TV"/></a></td>
<td align=left><a href="/details.php?id=1518421">Ольга [Season 2/Episode 9] [2017 / WEB-DL] [5.8/10]</a>
</td>
<td align="right">1</td>
<td align="right">0</td>
<td align=center width=20><nobr>21 ore</nobr></td>
<td align=center><nobr>300.36 MB</nobr></td>
<td align=right><a href=details.php?id=1518421&amp;toseeders=1><font color=#000000>347</font></a></td>
<td align=right><a href=details.php?id=1518421&amp;todlers=1>5</a></td>
<td align="right">34</td><td align=center nowrap><a href=userdetails.php?id=32199>V!ad</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=5"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_tv.gif" height="32" alt="TV"/></a></td>
<td align=left><a href="/details.php?id=1518420">Suits / Форс-мажоры [NewStudio] [Season 7/Episode 10] [2017 / WEB-DL] [8.6/10] [EN]</a>
</td>
<td align="right">1</td>
<td align="right">0</td>
<td align=center width=20><nobr>22 ore</nobr></td>
<td align=center><nobr>550.02 MB</nobr></td>
<td align=right><a href=details.php?id=1518420&amp;toseeders=1><font color=#000000>106</font></a></td>
<td align=right><a href=details.php?id=1518420&amp;todlers=1>2</a></td>
<td align="right">10</td><td align=center nowrap><a href=userdetails.php?id=32199>V!ad</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=5"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_tv.gif" height="32" alt="TV"/></a></td>
<td align=left><a href="/details.php?id=1518416">Suits / Форс-мажоры [Sunshine Studio] [Season 7/Episode 10] [2017 / WEB-DL] [8.6/10]</a>
</td>
<td align="right">1</td>
<td align="right">0</td>
<td align=center width=20><nobr>23 ore</nobr></td>
<td align=center><nobr>729.60 MB</nobr></td>
<td align=right><a href=details.php?id=1518416&amp;toseeders=1><font color=#000000>27</font></a></td>
<td align="right">0</td>
<td align="right">4</td><td align=center nowrap><a href=userdetails.php?id=121464>tomsim</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=1"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_movie.gif" height="32" alt="Movies"/></a></td>
<td align=left><a href="/details.php?id=1518415">Transformers: The Last Knight / Трансформеры: Последний рыцарь [2017 / BDRip] [Action / Adventure / Sci-Fi] [5.3/10]</a>
</td>
<td align="right">1</td>
<td align="right"><a href="details.php?id=1518415&amp;page=0#startcomments">5</a></td>
<td align=center width=20><nobr>09-14</nobr></td>
<td align=center><nobr>2.18 GB</nobr></td>
<td align=right><a href=details.php?id=1518415&amp;toseeders=1><font color=#000000>377</font></a></td>
<td align=right><a href=details.php?id=1518415&amp;todlers=1>38</a></td>
<td align="right">59</td><td align=center nowrap><a href=userdetails.php?id=32199>V!ad</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=18"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_hdtv.gif" height="29" alt="HDTV"/></a></td>
<td align=left><a href="/details.php?id=1518414" style="color:#707607">Transformers: The Last Knight / Трансформеры: Последний рыцарь [2017 / BDRip 720p] [Action / Adventure / Sci-Fi] [5.3/10] [EN]</a>
</td>
<td align="right">1</td>
<td align="right"><a href="details.php?id=1518414&amp;page=0#startcomments">4</a></td>
<td align=center width=20><nobr>09-14</nobr></td>
<td align=center><nobr>8.16 GB</nobr></td>
<td align=right><a href=details.php?id=1518414&amp;toseeders=1><font color=#000000>67</font></a></td>
<td align=right><a href=details.php?id=1518414&amp;todlers=1>10</a></td>
<td align="right">15</td><td align=center nowrap><a href=userdetails.php?id=32199>V!ad</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=1"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_movie.gif" height="32" alt="Movies"/></a></td>
<td align=left><a href="/details.php?id=1518413">Transformers: The Last Knight / Трансформеры: Последний рыцарь [2017 / BDRip] [Action / Adventure / Sci-Fi] [5.3/10]</a>
</td>
<td align="right">1</td>
<td align="right">0</td>
<td align=center width=20><nobr>09-14</nobr></td>
<td align=center><nobr>2.74 GB</nobr></td>
<td align=right><a href=details.php?id=1518413&amp;toseeders=1><font color=#000000>26</font></a></td>
<td align=right><a href=details.php?id=1518413&amp;todlers=1>4</a></td>
<td align="right">14</td><td align=center nowrap><a href=userdetails.php?id=32199>V!ad</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=1"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_movie.gif" height="32" alt="Movies"/></a></td>
<td align=left><a href="/details.php?id=1518412">Transformers: The Last Knight / Трансформеры: Последний рыцарь [2017 / BDRip] [Action / Adventure / Sci-Fi] [5.3/10]</a>
</td>
<td align="right">1</td>
<td align="right">0</td>
<td align=center width=20><nobr>09-14</nobr></td>
<td align=center><nobr>2.06 GB</nobr></td>
<td align=right><a href=details.php?id=1518412&amp;toseeders=1><font color=#000000>8</font></a></td>
<td align=right><a href=details.php?id=1518412&amp;todlers=1>2</a></td>
<td align="right">4</td><td align=center nowrap><a href=userdetails.php?id=32199>V!ad</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=5"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_tv.gif" height="32" alt="TV"/></a></td>
<td align=left><a href="/details.php?id=1518411"> Черная кровь [Episode 1-16] [2017 / SATRip]</a>
</td>
<td align="right"><a href="details.php?id=1518411&amp;filelist=1">16</a></td>
<td align="right">0</td>
<td align=center width=20><nobr>09-14</nobr></td>
<td align=center><nobr>10.70 GB</nobr></td>
<td align=right><a href=details.php?id=1518411&amp;toseeders=1><font color=#000000>38</font></a></td>
<td align=right><a href=details.php?id=1518411&amp;todlers=1>27</a></td>
<td align="right">10</td><td align=center nowrap><a href=userdetails.php?id=136958>anronn</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=5"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_tv.gif" height="32" alt="TV"/></a></td>
<td align=left><a href="/details.php?id=1518410">Импровизация [Season 3/Episode 11] [2017 / SATRip]</a>
</td>
<td align="right">1</td>
<td align="right">0</td>
<td align=center width=20><nobr>09-14</nobr></td>
<td align=center><nobr>648.31 MB</nobr></td>
<td align=right><a href=details.php?id=1518410&amp;toseeders=1><font color=#000000>140</font></a></td>
<td align=right><a href=details.php?id=1518410&amp;todlers=1>4</a></td>
<td align="right">12</td><td align=center nowrap><a href=userdetails.php?id=136958>anronn</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=2"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_music.gif" height="32" alt="Music"/></a></td>
<td align=left><a href="/details.php?id=1518409">VA - Pure Salinas, Vol. 8 (Compiled by DJ Zappi) [2017 / MP3 / 320] [House]</a>
</td>
<td align="right"><a href="details.php?id=1518409&amp;filelist=1">24</a></td>
<td align="right">0</td>
<td align=center width=20><nobr>09-14</nobr></td>
<td align=center><nobr>360.46 MB</nobr></td>
<td align=right><a href=details.php?id=1518409&amp;toseeders=1><font color=#000000>4</font></a></td>
<td align="right">0</td>
<td align="right">8</td><td align=center nowrap><a href=userdetails.php?id=710443>itsf8</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=4"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_games.gif" height="32" alt="Games"/></a></td>
<td align=left><a href="/details.php?id=1518408">Starpoint Gemini Warlords - Digital Deluxe Edition + Deadly Dozen DLC  [2017 / English] [Action] [EN]</a>
</td>
<td align="right"><a href="details.php?id=1518408&amp;filelist=1">9</a></td>
<td align="right"><a href="details.php?id=1518408&amp;page=0#startcomments">2</a></td>
<td align=center width=20><nobr>09-14</nobr></td>
<td align=center><nobr>5.76 GB</nobr></td>
<td align=right><a href=details.php?id=1518408&amp;toseeders=1><font color=#000000>3</font></a></td>
<td align=right><a href=details.php?id=1518408&amp;todlers=1>1</a></td>
<td align="right">4</td><td align=center nowrap><a href=userdetails.php?id=244541>RodionCB</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=18"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_hdtv.gif" height="29" alt="HDTV"/></a></td>
<td align=left><a href="/details.php?id=1518407" style="color:#707607">Молодёжка[720p] [Season 5 / Episode 10] [2017 / WEB-DL] [Drama / Sport] [5.4/10]</a>
</td>
<td align="right">1</td>
<td align="right">0</td>
<td align=center width=20><nobr>09-14</nobr></td>
<td align=center><nobr>1.23 GB</nobr></td>
<td align=right><a href=details.php?id=1518407&amp;toseeders=1><font color=#000000>22</font></a></td>
<td align="right">0</td>
<td align="right">3</td><td align=center nowrap><a href="./team.php?name=Millennium_Releasers_Group">MRG</a> / <a href=userdetails.php?id=6745>Малыш</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=17"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_sport.gif" height="32" alt="Sport"/></a></td>
<td align=left><a href="/details.php?id=1518406">Лига Чемпионов 2017-2018 / Групповой этап / 1-й тур / 2-й день / Обзор / Матч Футбол  [2017 / HDTVRip] [Soccer]</a>
</td>
<td align="right">1</td>
<td align="right">0</td>
<td align=center width=20><nobr>09-14</nobr></td>
<td align=center><nobr>626.19 MB</nobr></td>
<td align=right><a href=details.php?id=1518406&amp;toseeders=1><font color=#000000>69</font></a></td>
<td align=right><a href=details.php?id=1518406&amp;todlers=1>1</a></td>
<td align="right">17</td><td align=center nowrap><a href="./team.php?name=Millennium_Releasers_Group">MRG</a> / <a href=userdetails.php?id=6745>Малыш</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=5"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_tv.gif" height="32" alt="TV"/></a></td>
<td align=left><a href="/details.php?id=1518405">Молодёжка [Season 5/Episode 10] [2017 / WEB-DL] [5.4/10]</a>
</td>
<td align="right">1</td>
<td align="right"><a href="details.php?id=1518405&amp;page=0#startcomments">4</a></td>
<td align=center width=20><nobr>09-14</nobr></td>
<td align=center><nobr>600.55 MB</nobr></td>
<td align=right><a href=details.php?id=1518405&amp;toseeders=1><font color=#000000>204</font></a></td>
<td align=right><a href=details.php?id=1518405&amp;todlers=1>1</a></td>
<td align="right">14</td><td align=center nowrap><a href=userdetails.php?id=622367>FBR994</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=18"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_hdtv.gif" height="29" alt="HDTV"/></a></td>
<td align=left><a href="/details.php?id=1518403" style="color:#707607">Transformers: The Last Knight / Трансформеры: Последний рыцарь [720p] [2017 / WEB-DL] [Action / Adventure / Sci-Fi] [5.3/10]</a>
</td>
<td align="right">1</td>
<td align="right"><a href="details.php?id=1518403&amp;page=0#startcomments">2</a></td>
<td align=center width=20><nobr>09-13</nobr></td>
<td align=center><nobr>3.94 GB</nobr></td>
<td align=right><a href=details.php?id=1518403&amp;toseeders=1><font color=#000000>68</font></a></td>
<td align=right><a href=details.php?id=1518403&amp;todlers=1>2</a></td>
<td align="right">22</td><td align=center nowrap><a href=userdetails.php?id=32199>V!ad</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=1"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_movie.gif" height="32" alt="Movies"/></a></td>
<td align=left><a href="/details.php?id=1518402">Transformers: The Last Knight / Трансформеры: Последний рыцарь [2017 / WEB-DL] [Action / Adventure / Sci-Fi] [5.3/10]</a>
</td>
<td align="right">1</td>
<td align="right"><a href="details.php?id=1518402&amp;page=0#startcomments">2</a></td>
<td align=center width=20><nobr>09-13</nobr></td>
<td align=center><nobr>2.74 GB</nobr></td>
<td align=right><a href=details.php?id=1518402&amp;toseeders=1><font color=#000000>121</font></a></td>
<td align=right><a href=details.php?id=1518402&amp;todlers=1>1</a></td>
<td align="right">39</td><td align=center nowrap><a href=userdetails.php?id=32199>V!ad</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=1"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_movie.gif" height="32" alt="Movies"/></a></td>
<td align=left><a href="/details.php?id=1518399">Transformers: The Last Knight / Трансформеры: Последний рыцарь [2017 / WEB-DL] [Action / Adventure / Sci-Fi] [5.3/10]</a>
</td>
<td align="right">1</td>
<td align="right"><a href="details.php?id=1518399&amp;page=0#startcomments">7</a></td>
<td align=center width=20><nobr>09-13</nobr></td>
<td align=center><nobr>2.06 GB</nobr></td>
<td align=right><a href=details.php?id=1518399&amp;toseeders=1><font color=#000000>29</font></a></td>
<td align="right">0</td>
<td align="right">20</td><td align=center nowrap><a href=userdetails.php?id=32199>V!ad</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=5"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_tv.gif" height="32" alt="TV"/></a></td>
<td align=left><a href="/details.php?id=1518398">Отчий берег [Episode 5-6] [2017 / HDTVRip]</a>
</td>
<td align="right"><a href="details.php?id=1518398&amp;filelist=1">2</a></td>
<td align="right">0</td>
<td align=center width=20><nobr>09-13</nobr></td>
<td align=center><nobr>1.46 GB</nobr></td>
<td align=right><a href=details.php?id=1518398&amp;toseeders=1><font color=#000000>35</font></a></td>
<td align="right">0</td>
<td align="right">7</td><td align=center nowrap><a href=userdetails.php?id=622367>FBR994</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=1"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_movie.gif" height="32" alt="Movies"/></a></td>
<td align=left><a href="/details.php?id=1518397">Me casé con un boludo / Я вышла замуж за идиота [2016 / WEB-DL] [Comedy / Romance] [5.6/10]</a>
</td>
<td align="right">1</td>
<td align="right">0</td>
<td align=center width=20><nobr>09-13</nobr></td>
<td align=center><nobr>1.37 GB</nobr></td>
<td align=right><a href=details.php?id=1518397&amp;toseeders=1><font color=#000000>21</font></a></td>
<td align="right">0</td>
<td align="right">10</td><td align=center nowrap><a href=userdetails.php?id=136958>anronn</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=1"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_movie.gif" height="32" alt="Movies"/></a></td>
<td align=left><a href="/details.php?id=1518396">The House / Дом [2017 / WEB-DL] [Comedy] [5.5/10]</a>
</td>
<td align="right">1</td>
<td align="right"><a href="details.php?id=1518396&amp;page=0#startcomments">5</a></td>
<td align=center width=20><nobr>09-13</nobr></td>
<td align=center><nobr>1.37 GB</nobr></td>
<td align=right><a href=details.php?id=1518396&amp;toseeders=1><font color=#000000>159</font></a></td>
<td align=right><a href=details.php?id=1518396&amp;todlers=1>12</a></td>
<td align="right">25</td><td align=center nowrap><a href=userdetails.php?id=136958>anronn</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=5"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_tv.gif" height="32" alt="TV"/></a></td>
<td align=left><a href="/details.php?id=1518395">Tin Star / Стальная звезда (SunshineStudio) [Season 1/Episode 1-10] [2017 / WEBRip]</a>
</td>
<td align="right"><a href="details.php?id=1518395&amp;filelist=1">10</a></td>
<td align="right"><a href="details.php?id=1518395&amp;page=0#startcomments">3</a></td>
<td align=center width=20><nobr>09-13</nobr></td>
<td align=center><nobr>5.54 GB</nobr></td>
<td align=right><a href=details.php?id=1518395&amp;toseeders=1><font color=#000000>28</font></a></td>
<td align=right><a href=details.php?id=1518395&amp;todlers=1>6</a></td>
<td align="right">12</td><td align=center nowrap><a href=userdetails.php?id=293355>Partorg94</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=1"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_movie.gif" height="32" alt="Movies"/></a></td>
<td align=left><a href="/details.php?id=1518394">Pirates of the Caribbean: Dead Men Tell No Tales / Пираты Карибского моря: Мертвецы не рассказывают сказки [2017 / BDRip] [Action / Adventure / Sci-Fi] [6.9/10]</a>
</td>
<td align="right"><a href="details.php?id=1518394&amp;filelist=1">2</a></td>
<td align="right"><a href="details.php?id=1518394&amp;page=0#startcomments">2</a></td>
<td align=center width=20><nobr>09-13</nobr></td>
<td align=center><nobr>2.18 GB</nobr></td>
<td align=right><a href=details.php?id=1518394&amp;toseeders=1><font color=#000000>224</font></a></td>
<td align=right><a href=details.php?id=1518394&amp;todlers=1>16</a></td>
<td align="right">50</td><td align=center nowrap><a href=userdetails.php?id=136958>anronn</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=1"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_movie.gif" height="32" alt="Movies"/></a></td>
<td align=left><a href="/details.php?id=1518393">The Good Catholic / Хороший католик [2017 / WEB-DL] [Comedy / Drama] [5.3/10]</a>
</td>
<td align="right">1</td>
<td align="right"><a href="details.php?id=1518393&amp;page=0#startcomments">2</a></td>
<td align=center width=20><nobr>09-13</nobr></td>
<td align=center><nobr>1.36 GB</nobr></td>
<td align=right><a href=details.php?id=1518393&amp;toseeders=1><font color=#000000>13</font></a></td>
<td align="right">0</td>
<td align="right">4</td><td align=center nowrap><a href=userdetails.php?id=136958>anronn</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=1"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_movie.gif" height="32" alt="Movies"/></a></td>
<td align=left><a href="/details.php?id=1518392">The Ghoul / Упырь [2017 / BDRip] [Drama / Thriller] [5.7/10]</a>
</td>
<td align="right">1</td>
<td align="right">0</td>
<td align=center width=20><nobr>09-13</nobr></td>
<td align=center><nobr>1.35 GB</nobr></td>
<td align=right><a href=details.php?id=1518392&amp;toseeders=1><font color=#000000>33</font></a></td>
<td align=right><a href=details.php?id=1518392&amp;todlers=1>1</a></td>
<td align="right">7</td><td align=center nowrap><a href=userdetails.php?id=136958>anronn</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=1"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_movie.gif" height="32" alt="Movies"/></a></td>
<td align=left><a href="/details.php?id=1518391">#REALITYHIGH / #РЕАЛЬНАЯШКОЛА / Хештег &quot;Реальная Школа&quot;  [2017 / WEB-DL] [Comedy] [5.1/10]</a>
</td>
<td align="right">1</td>
<td align="right">0</td>
<td align=center width=20><nobr>09-13</nobr></td>
<td align=center><nobr>1.37 GB</nobr></td>
<td align=right><a href=details.php?id=1518391&amp;toseeders=1><font color=#000000>16</font></a></td>
<td align=right><a href=details.php?id=1518391&amp;todlers=1>2</a></td>
<td align="right">6</td><td align=center nowrap><a href=userdetails.php?id=136958>anronn</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=5"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_tv.gif" height="32" alt="TV"/></a></td>
<td align=left><a href="/details.php?id=1518390">The Strain / Штамм [AlexFilm] [Season 4/Episode 1-9] [2017 / WEB-DL] [7.4/10] [EN]</a>
</td>
<td align="right"><a href="details.php?id=1518390&amp;filelist=1">9</a></td>
<td align="right"><a href="details.php?id=1518390&amp;page=0#startcomments">2</a></td>
<td align=center width=20><nobr>09-13</nobr></td>
<td align=center><nobr>4.67 GB</nobr></td>
<td align=right><a href=details.php?id=1518390&amp;toseeders=1><font color=#000000>24</font></a></td>
<td align=right><a href=details.php?id=1518390&amp;todlers=1>12</a></td>
<td align="right">8</td><td align=center nowrap><a href="./team.php?name=Millennium_Releasers_Group">MRG</a> / <a href=userdetails.php?id=289277>Azarius</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=5"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_tv.gif" height="32" alt="TV"/></a></td>
<td align=left><a href="/details.php?id=1518389">Ольга [Season 2/Episode 8] [2017 / SATRip] [5.8/10]</a>
</td>
<td align="right">1</td>
<td align="right"><a href="details.php?id=1518389&amp;page=0#startcomments">2</a></td>
<td align=center width=20><nobr>09-13</nobr></td>
<td align=center><nobr>247.26 MB</nobr></td>
<td align=right><a href=details.php?id=1518389&amp;toseeders=1><font color=#000000>327</font></a></td>
<td align=right><a href=details.php?id=1518389&amp;todlers=1>3</a></td>
<td align="right">44</td><td align=center nowrap><a href=userdetails.php?id=136958>anronn</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=18"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_hdtv.gif" height="29" alt="HDTV"/></a></td>
<td align=left><a href="/details.php?id=1518388" style="color:#707607">Chefi la cuţite [Season 4 / Episode 2] [2017 / HDTVRip] [Family] [RO]</a>
</td>
<td align="right">1</td>
<td align="right">0</td>
<td align=center width=20><nobr>09-13</nobr></td>
<td align=center><nobr>1.36 GB</nobr></td>
<td align=right><a href=details.php?id=1518388&amp;toseeders=1><font color=#000000>31</font></a></td>
<td align=right><a href=details.php?id=1518388&amp;todlers=1>2</a></td>
<td align="right">11</td><td align=center nowrap><a href=userdetails.php?id=243055>phonestore</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=1"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_movie.gif" height="32" alt="Movies"/></a></td>
<td align=left><a href="/details.php?id=1518387">Birth of the Dragon / Брюс Ли: Рождение Дракона [2017 / CAM] [Action / Biography / Drama] [4.5/10]</a>
</td>
<td align="right">1</td>
<td align="right"><a href="details.php?id=1518387&amp;page=0#startcomments">1</a></td>
<td align=center width=20><nobr>09-13</nobr></td>
<td align=center><nobr>1.35 GB</nobr></td>
<td align=right><a href=details.php?id=1518387&amp;toseeders=1><font color=#000000>55</font></a></td>
<td align=right><a href=details.php?id=1518387&amp;todlers=1>3</a></td>
<td align="right">22</td><td align=center nowrap><a href=userdetails.php?id=359175>soulmusic</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=18"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_hdtv.gif" height="29" alt="HDTV"/></a></td>
<td align=left><a href="/details.php?id=1518386" style="color:#707607">It Comes at Night / Оно приходит ночью [2017 / BDRemux] [Horror / Detectiv] [6.4/10] [EN]</a>
</td>
<td align="right"><a href="details.php?id=1518386&amp;filelist=1">9</a></td>
<td align="right"><a href="details.php?id=1518386&amp;page=0#startcomments">2</a></td>
<td align=center width=20><nobr>09-13</nobr></td>
<td align=center><nobr>16.79 GB</nobr></td>
<td align=right><a href=details.php?id=1518386&amp;toseeders=1><font color=#000000>6</font></a></td>
<td align=right><a href=details.php?id=1518386&amp;todlers=1>3</a></td>
<td align="right">8</td><td align=center nowrap><a href=userdetails.php?id=105292>anatus</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=11"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_animation.gif" height="42" alt="Animation"/></a></td>
<td align=left><a href="/details.php?id=1518385">Les as de la jungle / Дозор джунглей [2017 / TELESYNC (TS)] [6.4/10]</a>
</td>
<td align="right">1</td>
<td align="right">0</td>
<td align=center width=20><nobr>09-13</nobr></td>
<td align=center><nobr>1.37 GB</nobr></td>
<td align=right><a href=details.php?id=1518385&amp;toseeders=1><font color=#000000>22</font></a></td>
<td align="right">0</td>
<td align="right">8</td><td align=center nowrap><a href=userdetails.php?id=136958>anronn</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=5"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_tv.gif" height="32" alt="TV"/></a></td>
<td align=left><a href="/details.php?id=1518384">Power / Власть в ночном городе [Amedia] [Season 4/Episode 10] [2017 / WEBRip] [8.2/10]</a>
</td>
<td align="right">1</td>
<td align="right">0</td>
<td align=center width=20><nobr>09-13</nobr></td>
<td align=center><nobr>700.31 MB</nobr></td>
<td align=right><a href=details.php?id=1518384&amp;toseeders=1><font color=#000000>16</font></a></td>
<td align="right">0</td>
<td align="right">5</td><td align=center nowrap><a href="./team.php?name=Educational_Seed_Team">EDU</a> / <a href=userdetails.php?id=650380>ZarjSD</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=4"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_games.gif" height="32" alt="Games"/></a></td>
<td align=left><a href="/details.php?id=1518383">F1 2017 (Codemasters) (RUS|ENG|MULTi10) [L]  [2017] [Simulation]</a>
</td>
<td align="right"><a href="details.php?id=1518383&amp;filelist=1">2</a></td>
<td align="right"><a href="details.php?id=1518383&amp;page=0#startcomments">6</a></td>
<td align=center width=20><nobr>09-13</nobr></td>
<td align=center><nobr>34.19 GB</nobr></td>
<td align=right><a href=details.php?id=1518383&amp;toseeders=1><font color=#000000>7</font></a></td>
<td align=right><a href=details.php?id=1518383&amp;todlers=1>2</a></td>
<td align="right">14</td><td align=center nowrap><a href="./team.php?name=Top_Seed_Team">TST</a> / <a href=userdetails.php?id=668581>Ankiler</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=5"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_tv.gif" height="32" alt="TV"/></a></td>
<td align=left><a href="/details.php?id=1518382">Preacher  / Проповедник(SunshineStudio) [Season 2/Episode 12] [2017 / HDTVRip]</a>
</td>
<td align="right">1</td>
<td align="right">0</td>
<td align=center width=20><nobr>09-13</nobr></td>
<td align=center><nobr>570.27 MB</nobr></td>
<td align=right><a href=details.php?id=1518382&amp;toseeders=1><font color=#000000>18</font></a></td>
<td align="right">0</td>
<td align="right">4</td><td align=center nowrap><a href=userdetails.php?id=293355>Partorg94</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=1"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_movie.gif" height="32" alt="Movies"/></a></td>
<td align=left><a href="/details.php?id=1518380">Dragonheart: Battle for the Heartfire / Сердце дракона 4 [2017 / BDRip] [Fantasy] [5.2/10]</a>
</td>
<td align="right">1</td>
<td align="right"><a href="details.php?id=1518380&amp;page=0#startcomments">1</a></td>
<td align=center width=20><nobr>09-13</nobr></td>
<td align=center><nobr>1.46 GB</nobr></td>
<td align=right><a href=details.php?id=1518380&amp;toseeders=1><font color=#000000>23</font></a></td>
<td align=right><a href=details.php?id=1518380&amp;todlers=1>3</a></td>
<td align="right">13</td><td align=center nowrap><a href=userdetails.php?id=136958>anronn</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=1"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_movie.gif" height="32" alt="Movies"/></a></td>
<td align=left><a href="/details.php?id=1518379">Snatched / Дочь и мать её [2017 / BDRip] [Action / Comedy] [4.2/10]</a>
</td>
<td align="right">1</td>
<td align="right"><a href="details.php?id=1518379&amp;page=0#startcomments">1</a></td>
<td align=center width=20><nobr>09-13</nobr></td>
<td align=center><nobr>1.46 GB</nobr></td>
<td align=right><a href=details.php?id=1518379&amp;toseeders=1><font color=#000000>52</font></a></td>
<td align=right><a href=details.php?id=1518379&amp;todlers=1>1</a></td>
<td align="right">15</td><td align=center nowrap><a href=userdetails.php?id=136958>anronn</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=18"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_hdtv.gif" height="29" alt="HDTV"/></a></td>
<td align=left><a href="/details.php?id=1518378" style="color:#707607">Молодёжка[720p] [Season 5 / Episode 9] [2017 / WEB-DL] [Drama / Sport] [5.4/10]</a>
</td>
<td align="right">1</td>
<td align="right">0</td>
<td align=center width=20><nobr>09-13</nobr></td>
<td align=center><nobr>1.22 GB</nobr></td>
<td align=right><a href=details.php?id=1518378&amp;toseeders=1><font color=#000000>25</font></a></td>
<td align="right">0</td>
<td align="right">2</td><td align=center nowrap><a href=userdetails.php?id=622367>FBR994</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=5"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_tv.gif" height="32" alt="TV"/></a></td>
<td align=left><a href="/details.php?id=1518377">Молодёжка [Season 5/Episode 9] [2017 / WEB-DL] [5.4/10]</a>
</td>
<td align="right">1</td>
<td align="right"><a href="details.php?id=1518377&amp;page=0#startcomments">7</a></td>
<td align=center width=20><nobr>09-13</nobr></td>
<td align=center><nobr>599.93 MB</nobr></td>
<td align=right><a href=details.php?id=1518377&amp;toseeders=1><font color=#000000>175</font></a></td>
<td align="right">0</td>
<td align="right">16</td><td align=center nowrap><a href=userdetails.php?id=622367>FBR994</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=17"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_sport.gif" height="32" alt="Sport"/></a></td>
<td align=left><a href="/details.php?id=1518375">Лига Чемпионов 2017-2018 / Групповой этап / 1-й тур / 1-й день / Обзор / Матч Футбол  [2017 / HDTVRip] [Soccer]</a>
</td>
<td align="right">1</td>
<td align="right">0</td>
<td align=center width=20><nobr>09-13</nobr></td>
<td align=center><nobr>737.75 MB</nobr></td>
<td align=right><a href=details.php?id=1518375&amp;toseeders=1><font color=#000000>80</font></a></td>
<td align=right><a href=details.php?id=1518375&amp;todlers=1>1</a></td>
<td align="right">25</td><td align=center nowrap><a href="./team.php?name=Millennium_Releasers_Group">MRG</a> / <a href=userdetails.php?id=6745>Малыш</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=18"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_hdtv.gif" height="29" alt="HDTV"/></a></td>
<td align=left><a href="/details.php?id=1518374" style="color:#707607">Pirates of the Caribbean: Dead Men Tell No Tales / Пираты Карибского моря: Мертвецы не рассказывают сказки [2017 / BDRip 1080p] [Action / Adventure / Fantasy] [6.9/10] [EN]</a>
</td>
<td align="right">1</td>
<td align="right"><a href="details.php?id=1518374&amp;page=0#startcomments">4</a></td>
<td align=center width=20><nobr>09-12</nobr></td>
<td align=center><nobr>11.51 GB</nobr></td>
<td align=right><a href=details.php?id=1518374&amp;toseeders=1><font color=#000000>209</font></a></td>
<td align=right><a href=details.php?id=1518374&amp;todlers=1>22</a></td>
<td align="right">77</td><td align=center nowrap><a href=userdetails.php?id=221427>axweel</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=1"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_movie.gif" height="32" alt="Movies"/></a></td>
<td align=left><a href="/details.php?id=1518373">Pirates of the Caribbean: Dead Men Tell No Tales / Пираты Карибского моря: Мертвецы не рассказывают сказки [2017 / BDRip] [Action / Adventure / Sci-Fi] [6.9/10]</a>
</td>
<td align="right">1</td>
<td align="right"><a href="details.php?id=1518373&amp;page=0#startcomments">4</a></td>
<td align=center width=20><nobr>09-12</nobr></td>
<td align=center><nobr>1.37 GB</nobr></td>
<td align=right><a href=details.php?id=1518373&amp;toseeders=1><font color=#000000>293</font></a></td>
<td align=right><a href=details.php?id=1518373&amp;todlers=1>19</a></td>
<td align="right">87</td><td align=center nowrap><a href=userdetails.php?id=32199>V!ad</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=1"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_movie.gif" height="32" alt="Movies"/></a></td>
<td align=left><a href="/details.php?id=1518372">Pirates of the Caribbean: Dead Men Tell No Tales  / Пираты Карибского моря: Мертвецы не рассказывают сказки  [2017 / HDTVRip] [Action / Adventure / Fantasy] [6.9/10]</a>
</td>
<td align="right">1</td>
<td align="right">0</td>
<td align=center width=20><nobr>09-12</nobr></td>
<td align=center><nobr>2.05 GB</nobr></td>
<td align=right><a href=details.php?id=1518372&amp;toseeders=1><font color=#000000>64</font></a></td>
<td align=right><a href=details.php?id=1518372&amp;todlers=1>1</a></td>
<td align="right">26</td><td align=center nowrap><a href=userdetails.php?id=221427>axweel</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=5"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_tv.gif" height="32" alt="TV"/></a></td>
<td align=left><a href="/details.php?id=1518371">Отчий берег [Episode 1-4] [2017 / HDTVRip]</a>
</td>
<td align="right"><a href="details.php?id=1518371&amp;filelist=1">4</a></td>
<td align="right">0</td>
<td align=center width=20><nobr>09-12</nobr></td>
<td align=center><nobr>2.94 GB</nobr></td>
<td align=right><a href=details.php?id=1518371&amp;toseeders=1><font color=#000000>53</font></a></td>
<td align=right><a href=details.php?id=1518371&amp;todlers=1>8</a></td>
<td align="right">18</td><td align=center nowrap><a href=userdetails.php?id=622367>FBR994</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=1"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_movie.gif" height="32" alt="Movies"/></a></td>
<td align=left><a href="/details.php?id=1518369">Swap / Боевой механизм [2016 / BDRip] [Action / Sci-Fi / Thriller] [4.4/10]</a>
</td>
<td align="right">1</td>
<td align="right"><a href="details.php?id=1518369&amp;page=0#startcomments">1</a></td>
<td align=center width=20><nobr>09-12</nobr></td>
<td align=center><nobr>1.37 GB</nobr></td>
<td align=right><a href=details.php?id=1518369&amp;toseeders=1><font color=#000000>50</font></a></td>
<td align=right><a href=details.php?id=1518369&amp;todlers=1>4</a></td>
<td align="right">18</td><td align=center nowrap><a href=userdetails.php?id=136958>anronn</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=18"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_hdtv.gif" height="29" alt="HDTV"/></a></td>
<td align=left><a href="/details.php?id=1518370" style="color:#707607">Pirates of the Caribbean: Dead Men Tell No Tales / Пираты Карибского моря: Мертвецы не рассказывают сказки [2017 / Blu-Ray] [Action / Adventure / Fantasy] [6.9/10] [EN]</a>
</td>
<td align="right"><a href="details.php?id=1518370&amp;filelist=1">1238</a></td>
<td align="right"><a href="details.php?id=1518370&amp;page=0#startcomments">9</a></td>
<td align=center width=20><nobr>09-12</nobr></td>
<td align=center><nobr>42.24 GB</nobr></td>
<td align=right><a href=details.php?id=1518370&amp;toseeders=1><font color=#000000>14</font></a></td>
<td align=right><a href=details.php?id=1518370&amp;todlers=1>2</a></td>
<td align="right">23</td><td align=center nowrap><a href="./team.php?name=TOTAL_UPLOADERS_TEAM">TUT</a> / <a href=userdetails.php?id=331407>Marchelush</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=1"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_movie.gif" height="32" alt="Movies"/></a></td>
<td align=left><a href="/details.php?id=1518368">Picture of Beauty / Картина красоты [2017 / BDRip] [Drama / Romance] [4.8/10]</a>
</td>
<td align="right">1</td>
<td align="right"><a href="details.php?id=1518368&amp;page=0#startcomments">4</a></td>
<td align=center width=20><nobr>09-12</nobr></td>
<td align=center><nobr>1.14 GB</nobr></td>
<td align=right><a href=details.php?id=1518368&amp;toseeders=1><font color=#000000>21</font></a></td>
<td align="right">0</td>
<td align="right">9</td><td align=center nowrap><a href=userdetails.php?id=136958>anronn</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=2"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_music.gif" height="32" alt="Music"/></a></td>
<td align=left><a href="/details.php?id=1518367">VA - Top 100 Beatport Downloads August [2017 / MP3 / 320] [House]</a>
</td>
<td align="right"><a href="details.php?id=1518367&amp;filelist=1">100</a></td>
<td align="right"><a href="details.php?id=1518367&amp;page=0#startcomments">2</a></td>
<td align=center width=20><nobr>09-12</nobr></td>
<td align=center><nobr>1.46 GB</nobr></td>
<td align=right><a href=details.php?id=1518367&amp;toseeders=1><font color=#000000>34</font></a></td>
<td align="right">0</td>
<td align="right">20</td><td align=center nowrap><a href=userdetails.php?id=54073>mcfg</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=18"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_hdtv.gif" height="29" alt="HDTV"/></a></td>
<td align=left><a href="/details.php?id=1518366" style="color:#707607">Chefi la cuţite [Season 4 / Episode 1] [2017 / HDTVRip] [Family] [RO]</a>
</td>
<td align="right">1</td>
<td align="right">0</td>
<td align=center width=20><nobr>09-12</nobr></td>
<td align=center><nobr>1.36 GB</nobr></td>
<td align=right><a href=details.php?id=1518366&amp;toseeders=1><font color=#000000>36</font></a></td>
<td align=right><a href=details.php?id=1518366&amp;todlers=1>3</a></td>
<td align="right">14</td><td align=center nowrap><a href=userdetails.php?id=243055>phonestore</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=2"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_music.gif" height="32" alt="Music"/></a></td>
<td align=left><a href="/details.php?id=1518365">VA - Trance In Motion Volume 223 (Mixed by Emil Sorous) [2017 / MP3 / 320] [Trance]</a>
</td>
<td align="right"><a href="details.php?id=1518365&amp;filelist=1">4</a></td>
<td align="right"><a href="details.php?id=1518365&amp;page=0#startcomments">1</a></td>
<td align=center width=20><nobr>09-12</nobr></td>
<td align=center><nobr>200.33 MB</nobr></td>
<td align=right><a href=details.php?id=1518365&amp;toseeders=1><font color=#000000>5</font></a></td>
<td align="right">0</td>
<td align="right">6</td><td align=center nowrap><a href="./team.php?name=Music_Seed_Team">MST</a> / <a href=userdetails.php?id=633692>Novopassit</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=5"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_tv.gif" height="32" alt="TV"/></a></td>
<td align=left><a href="/details.php?id=1518364">Ольга [Season 2/Episode 7] [2017 / SATRip] [5.8/10]</a>
</td>
<td align="right">1</td>
<td align="right">0</td>
<td align=center width=20><nobr>09-12</nobr></td>
<td align=center><nobr>263.89 MB</nobr></td>
<td align=right><a href=details.php?id=1518364&amp;toseeders=1><font color=#000000>296</font></a></td>
<td align=right><a href=details.php?id=1518364&amp;todlers=1>2</a></td>
<td align="right">48</td><td align=center nowrap><a href=userdetails.php?id=136958>anronn</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=1"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_movie.gif" height="32" alt="Movies"/></a></td>
<td align=left><a href="/details.php?id=1518362"> Pirates of the Caribbean: Dead Men Tell No Tales /  Пираты Карибского моря: Мертвецы не рассказывают сказки [2017 / BDRip] [Action / Adventure / Sci-Fi] [6.9/10]</a>
</td>
<td align="right">1</td>
<td align="right"><a href="details.php?id=1518362&amp;page=0#startcomments">3</a></td>
<td align=center width=20><nobr>09-12</nobr></td>
<td align=center><nobr>2.05 GB</nobr></td>
<td align=right><a href=details.php?id=1518362&amp;toseeders=1><font color=#000000>50</font></a></td>
<td align=right><a href=details.php?id=1518362&amp;todlers=1>1</a></td>
<td align="right">23</td><td align=center nowrap><a href=userdetails.php?id=136958>anronn</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=1"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_movie.gif" height="32" alt="Movies"/></a></td>
<td align=left><a href="/details.php?id=1518363">Pirates of the Caribbean: Dead Men Tell No Tales / Пираты Карибского моря: Мертвецы не рассказывают сказки [2017 / BDRip] [Action / Adventure / Sci-Fi] [6.9/10]</a>
</td>
<td align="right">1</td>
<td align="right">0</td>
<td align=center width=20><nobr>09-12</nobr></td>
<td align=center><nobr>1.37 GB</nobr></td>
<td align=right><a href=details.php?id=1518363&amp;toseeders=1><font color=#000000>25</font></a></td>
<td align=right><a href=details.php?id=1518363&amp;todlers=1>1</a></td>
<td align="right">10</td><td align=center nowrap><a href=userdetails.php?id=136958>anronn</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=1"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_movie.gif" height="32" alt="Movies"/></a></td>
<td align=left><a href="/details.php?id=1518361"> Baby Driver / Малыш на драйве [2017 / WEB-DL] [Action / Crime / Thriller] [8.1/10]</a>
</td>
<td align="right">1</td>
<td align="right"><a href="details.php?id=1518361&amp;page=0#startcomments">14</a></td>
<td align=center width=20><nobr>09-12</nobr></td>
<td align=center><nobr>1.46 GB</nobr></td>
<td align=right><a href=details.php?id=1518361&amp;toseeders=1><font color=#000000>369</font></a></td>
<td align=right><a href=details.php?id=1518361&amp;todlers=1>7</a></td>
<td align="right">57</td><td align=center nowrap><a href=userdetails.php?id=136958>anronn</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=2"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_music.gif" height="32" alt="Music"/></a></td>
<td align=left><a href="/details.php?id=1518360">Каспийский Груз  - «Саундтрек к так и не снятому фильму» [2017 / MP3 / 320] [Rap]</a>
</td>
<td align="right"><a href="details.php?id=1518360&amp;filelist=1">16</a></td>
<td align="right"><a href="details.php?id=1518360&amp;page=0#startcomments">1</a></td>
<td align=center width=20><nobr>09-12</nobr></td>
<td align=center><nobr>162.93 MB</nobr></td>
<td align=right><a href=details.php?id=1518360&amp;toseeders=1><font color=#000000>56</font></a></td>
<td align=right><a href=details.php?id=1518360&amp;todlers=1>1</a></td>
<td align="right">30</td><td align=center nowrap><a href=userdetails.php?id=563471>Mafioznick</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=11"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_animation.gif" height="42" alt="Animation"/></a></td>
<td align=left><a href="/details.php?id=1518359">Starship Troopers: Traitor of Mars / Звёздный десант: Предатель Марса  [2017 / BDRip] [5.5/10]</a>
</td>
<td align="right">1</td>
<td align="right">0</td>
<td align=center width=20><nobr>09-12</nobr></td>
<td align=center><nobr>1.37 GB</nobr></td>
<td align=right><a href=details.php?id=1518359&amp;toseeders=1><font color=#000000>28</font></a></td>
<td align="right">0</td>
<td align="right">17</td><td align=center nowrap><a href=userdetails.php?id=136958>anronn</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=2"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_music.gif" height="32" alt="Music"/></a></td>
<td align=left><a href="/details.php?id=1518358">Cabron - Lupu&#039; DPM [2017 / MP3 / 320] [Hip-Hop]</a>
</td>
<td align="right"><a href="details.php?id=1518358&amp;filelist=1">19</a></td>
<td align="right">0</td>
<td align=center width=20><nobr>09-12</nobr></td>
<td align=center><nobr>141.90 MB</nobr></td>
<td align=right><a href=details.php?id=1518358&amp;toseeders=1><font color=#000000>22</font></a></td>
<td align="right">0</td>
<td align="right">15</td><td align=center nowrap><a href=userdetails.php?id=710443>itsf8</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=1"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_movie.gif" height="32" alt="Movies"/></a></td>
<td align=left><a href="/details.php?id=1518352">It Had to Be You / Им должен быть ты [2015 / WEB-DL] [Comedy / Romance / Music] [5.5/10]</a>
</td>
<td align="right">1</td>
<td align="right">0</td>
<td align=center width=20><nobr>09-12</nobr></td>
<td align=center><nobr>1.37 GB</nobr></td>
<td align=right><a href=details.php?id=1518352&amp;toseeders=1><font color=#000000>13</font></a></td>
<td align="right">0</td>
<td align="right">7</td><td align=center nowrap><a href=userdetails.php?id=136958>anronn</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=2"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_music.gif" height="32" alt="Music"/></a></td>
<td align=left><a href="/details.php?id=1518348">VA - Greek Remixes Collection Vol.1  [2017 / MP3 / 320] [Dance]</a>
</td>
<td align="right"><a href="details.php?id=1518348&amp;filelist=1">26</a></td>
<td align="right">0</td>
<td align=center width=20><nobr>09-12</nobr></td>
<td align=center><nobr>197.51 MB</nobr></td>
<td align=right><a href=details.php?id=1518348&amp;toseeders=1><font color=#000000>8</font></a></td>
<td align="right">0</td>
<td align="right">8</td><td align=center nowrap><a href=userdetails.php?id=777705>masterdj2011</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=1"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_movie.gif" height="32" alt="Movies"/></a></td>
<td align=left><a href="/details.php?id=1518357">Plug Love / Опасная любовь [2017 / WEB-DL] [Drama] [7.3/10]</a>
</td>
<td align="right">1</td>
<td align="right"><a href="details.php?id=1518357&amp;page=0#startcomments">2</a></td>
<td align=center width=20><nobr>09-12</nobr></td>
<td align=center><nobr>1.46 GB</nobr></td>
<td align=right><a href=details.php?id=1518357&amp;toseeders=1><font color=#000000>12</font></a></td>
<td align=right><a href=details.php?id=1518357&amp;todlers=1>1</a></td>
<td align="right">6</td><td align=center nowrap><a href=userdetails.php?id=136958>anronn</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=2"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_music.gif" height="32" alt="Music"/></a></td>
<td align=left><a href="/details.php?id=1518356">VA - Best Romanian Summer Hits 2017 [2017 / MP3 / 320] [Dance]</a>
</td>
<td align="right"><a href="details.php?id=1518356&amp;filelist=1">82</a></td>
<td align="right">0</td>
<td align=center width=20><nobr>09-12</nobr></td>
<td align=center><nobr>597.19 MB</nobr></td>
<td align=right><a href=details.php?id=1518356&amp;toseeders=1><font color=#000000>78</font></a></td>
<td align="right">0</td>
<td align="right">38</td><td align=center nowrap><a href=userdetails.php?id=777705>masterdj2011</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=1"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_movie.gif" height="32" alt="Movies"/></a></td>
<td align=left><a href="/details.php?id=1518355">Norman: The Moderate Rise and Tragic Fall of a New York Fixer / Стратегия Оппенгеймера [2016 / BDRip] [Thriller / Drama] [6.3/10]</a>
</td>
<td align="right"><a href="details.php?id=1518355&amp;filelist=1">2</a></td>
<td align="right">0</td>
<td align=center width=20><nobr>09-12</nobr></td>
<td align=center><nobr>1.41 GB</nobr></td>
<td align=right><a href=details.php?id=1518355&amp;toseeders=1><font color=#000000>35</font></a></td>
<td align=right><a href=details.php?id=1518355&amp;todlers=1>2</a></td>
<td align="right">16</td><td align=center nowrap><a href=userdetails.php?id=136958>anronn</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=1"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_movie.gif" height="32" alt="Movies"/></a></td>
<td align=left><a href="/details.php?id=1518354">47 Meters Down / Синяя бездна [2017 / WEB-DL] [Adventure / Thriller / Horror] [5.8/10]</a>
</td>
<td align="right">1</td>
<td align="right"><a href="details.php?id=1518354&amp;page=0#startcomments">5</a></td>
<td align=center width=20><nobr>09-12</nobr></td>
<td align=center><nobr>1.46 GB</nobr></td>
<td align=right><a href=details.php?id=1518354&amp;toseeders=1><font color=#000000>92</font></a></td>
<td align=right><a href=details.php?id=1518354&amp;todlers=1>2</a></td>
<td align="right">35</td><td align=center nowrap><a href=userdetails.php?id=136958>anronn</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=1"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_movie.gif" height="32" alt="Movies"/></a></td>
<td align=left><a href="/details.php?id=1518353">Pokot / След зверя [2017 / BDRip] [Crime / Thriller / Detectiv] [6.5/10]</a>
</td>
<td align="right">1</td>
<td align="right">0</td>
<td align=center width=20><nobr>09-12</nobr></td>
<td align=center><nobr>2.05 GB</nobr></td>
<td align=right><a href=details.php?id=1518353&amp;toseeders=1><font color=#000000>94</font></a></td>
<td align=right><a href=details.php?id=1518353&amp;todlers=1>3</a></td>
<td align="right">45</td><td align=center nowrap><a href=userdetails.php?id=136958>anronn</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=17"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_sport.gif" height="32" alt="Sport"/></a></td>
<td align=left><a href="/details.php?id=1518350">WWE Smackdown Live (Русская версия от 545TV) [05.09] [2017 / HDTVRip] [Wrestling]</a>
</td>
<td align="right">1</td>
<td align="right">0</td>
<td align=center width=20><nobr>09-11</nobr></td>
<td align=center><nobr>870.04 MB</nobr></td>
<td align=right><a href=details.php?id=1518350&amp;toseeders=1><font color=#000000>1</font></a></td>
<td align="right">0</td>
<td align="right">2</td><td align=center nowrap><a href=userdetails.php?id=520915>cprofire</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=17"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_sport.gif" height="32" alt="Sport"/></a></td>
<td align=left><a href="/details.php?id=1518349">WWE Monday Night RAW (Русская версия от 545TV) [04/09] [2017 / HDTVRip] [Wrestling]</a>
</td>
<td align="right">1</td>
<td align="right">0</td>
<td align=center width=20><nobr>09-11</nobr></td>
<td align=center><nobr>1.47 GB</nobr></td>
<td align=right><a href=details.php?id=1518349&amp;toseeders=1><font color=#000000>2</font></a></td>
<td align="right">0</td>
<td align="right">3</td><td align=center nowrap><a href=userdetails.php?id=520915>cprofire</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=1"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_movie.gif" height="32" alt="Movies"/></a></td>
<td align=left><a href="/details.php?id=1518347">Toy Soldiers / Soldați de ocazie [audio română] [1991 / BDRip] [Action / Thriller / Drama] [6.5/10] [RO]</a>
</td>
<td align="right">1</td>
<td align="right"><a href="details.php?id=1518347&amp;page=0#startcomments">1</a></td>
<td align=center width=20><nobr>09-11</nobr></td>
<td align=center><nobr>1.67 GB</nobr></td>
<td align=right><a href=details.php?id=1518347&amp;toseeders=1><font color=#000000>10</font></a></td>
<td align="right">0</td>
<td align="right">12</td><td align=center nowrap><a href="./team.php?name=Romanian_Content_Team">RCT</a> / <a href=userdetails.php?id=696686>Rodika1989</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=2"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_music.gif" height="32" alt="Music"/></a></td>
<td align=left><a href="/details.php?id=1518345">VA - Boom Hits Vol.768 - 2017 [2017 / MP3 / 320] [Dance]</a>
</td>
<td align="right"><a href="details.php?id=1518345&amp;filelist=1">42</a></td>
<td align="right">0</td>
<td align=center width=20><nobr>09-11</nobr></td>
<td align=center><nobr>315.22 MB</nobr></td>
<td align=right><a href=details.php?id=1518345&amp;toseeders=1><font color=#000000>27</font></a></td>
<td align=right><a href=details.php?id=1518345&amp;todlers=1>1</a></td>
<td align="right">13</td><td align=center nowrap><a href=userdetails.php?id=777705>masterdj2011</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=5"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_tv.gif" height="32" alt="TV"/></a></td>
<td align=left><a href="/details.php?id=1518346">Однажды в России [Season 6/Episode 2] [2017 / SATRip]</a>
</td>
<td align="right">1</td>
<td align="right"><a href="details.php?id=1518346&amp;page=0#startcomments">2</a></td>
<td align=center width=20><nobr>09-11</nobr></td>
<td align=center><nobr>595.99 MB</nobr></td>
<td align=right><a href=details.php?id=1518346&amp;toseeders=1><font color=#000000>96</font></a></td>
<td align=right><a href=details.php?id=1518346&amp;todlers=1>1</a></td>
<td align="right">21</td><td align=center nowrap><a href=userdetails.php?id=136958>anronn</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=5"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_tv.gif" height="32" alt="TV"/></a></td>
<td align=left><a href="/details.php?id=1518344">Ольга [Season 2/Episode 6] [2017 / SATRip]</a>
</td>
<td align="right">1</td>
<td align="right">0</td>
<td align=center width=20><nobr>09-11</nobr></td>
<td align=center><nobr>302.80 MB</nobr></td>
<td align=right><a href=details.php?id=1518344&amp;toseeders=1><font color=#000000>269</font></a></td>
<td align=right><a href=details.php?id=1518344&amp;todlers=1>1</a></td>
<td align="right">45</td><td align=center nowrap><a href=userdetails.php?id=136958>anronn</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=1"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_movie.gif" height="32" alt="Movies"/></a></td>
<td align=left><a href="/details.php?id=1518343">Cage Dive / Над глубиной: Хроника выживания [2017 / WEB-DL] [Thriller / Horror / Drama] [4.2/10]</a>
</td>
<td align="right">1</td>
<td align="right"><a href="details.php?id=1518343&amp;page=0#startcomments">7</a></td>
<td align=center width=20><nobr>09-11</nobr></td>
<td align=center><nobr>1.37 GB</nobr></td>
<td align=right><a href=details.php?id=1518343&amp;toseeders=1><font color=#000000>103</font></a></td>
<td align=right><a href=details.php?id=1518343&amp;todlers=1>1</a></td>
<td align="right">39</td><td align=center nowrap><a href=userdetails.php?id=136958>anronn</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=18"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_hdtv.gif" height="29" alt="HDTV"/></a></td>
<td align=left><a href="/details.php?id=1518342" style="color:#707607">Vocea României [720p] [Season 7 / Episode 2] [2017 / WEB-DL] [Music] [RO]</a>
</td>
<td align="right">1</td>
<td align="right"><a href="details.php?id=1518342&amp;page=0#startcomments">5</a></td>
<td align=center width=20><nobr>09-11</nobr></td>
<td align=center><nobr>1.21 GB</nobr></td>
<td align=right><a href=details.php?id=1518342&amp;toseeders=1><font color=#000000>90</font></a></td>
<td align="right">0</td>
<td align="right">34</td><td align=center nowrap><a href=userdetails.php?id=441089>Nonconformist</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=2"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_music.gif" height="32" alt="Music"/></a></td>
<td align=left><a href="/details.php?id=1518341">VA - Sports Megamix 2017.2 [2017 / MP3 / 320] [Dance]</a>
</td>
<td align="right"><a href="details.php?id=1518341&amp;filelist=1">106</a></td>
<td align="right"><a href="details.php?id=1518341&amp;page=0#startcomments">1</a></td>
<td align=center width=20><nobr>09-11</nobr></td>
<td align=center><nobr>533.55 MB</nobr></td>
<td align=right><a href=details.php?id=1518341&amp;toseeders=1><font color=#000000>36</font></a></td>
<td align=right><a href=details.php?id=1518341&amp;todlers=1>1</a></td>
<td align="right">33</td><td align=center nowrap><a href=userdetails.php?id=710443>itsf8</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=17"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_sport.gif" height="32" alt="Sport"/></a></td>
<td align=left><a href="/details.php?id=1518340">WWE Summerslam 2017 (Русская версия от 545TV) [20/08] [2017 / WEB-DL] [Wrestling]</a>
</td>
<td align="right">1</td>
<td align="right"><a href="details.php?id=1518340&amp;page=0#startcomments">2</a></td>
<td align=center width=20><nobr>09-11</nobr></td>
<td align=center><nobr>3.09 GB</nobr></td>
<td align=right><a href=details.php?id=1518340&amp;toseeders=1><font color=#000000>4</font></a></td>
<td align="right">0</td>
<td align="right">6</td><td align=center nowrap><a href=userdetails.php?id=441089>Nonconformist</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=18"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_hdtv.gif" height="29" alt="HDTV"/></a></td>
<td align=left><a href="/details.php?id=1518339" style="color:#707607">The Expanse / Expansiunea [audio română] [Season 1 / Episode 1-10] [2015 / BDRip 720p] [Sci-Fi / Thriller / Drama] [8.3/10] [RO] [EN]</a>
</td>
<td align="right"><a href="details.php?id=1518339&amp;filelist=1">10</a></td>
<td align="right"><a href="details.php?id=1518339&amp;page=0#startcomments">7</a></td>
<td align=center width=20><nobr>09-11</nobr></td>
<td align=center><nobr>19.49 GB</nobr></td>
<td align=right><a href=details.php?id=1518339&amp;toseeders=1><font color=#000000>11</font></a></td>
<td align=right><a href=details.php?id=1518339&amp;todlers=1>3</a></td>
<td align="right">27</td><td align=center nowrap><a href="./team.php?name=Romanian_Content_Team">RCT</a> / <a href=userdetails.php?id=696686>Rodika1989</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=13"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_movie_doc.gif" height="32" alt="Movies Documentary"/></a></td>
<td align=left><a href="/details.php?id=1518338">Lumière! / Люмьеры! [2016 / WEB-DL] [8.4/10]</a>
</td>
<td align="right">1</td>
<td align="right">0</td>
<td align=center width=20><nobr>09-11</nobr></td>
<td align=center><nobr>1.37 GB</nobr></td>
<td align=right><a href=details.php?id=1518338&amp;toseeders=1><font color=#000000>23</font></a></td>
<td align="right">0</td>
<td align="right">16</td><td align=center nowrap><a href=userdetails.php?id=136958>anronn</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=1"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_movie.gif" height="32" alt="Movies"/></a></td>
<td align=left><a href="/details.php?id=1518337">Anti Matter / Антиматерия [2016 / WEB-DL] [Sci-Fi] [7.9/10]</a>
</td>
<td align="right">1</td>
<td align="right"><a href="details.php?id=1518337&amp;page=0#startcomments">3</a></td>
<td align=center width=20><nobr>09-11</nobr></td>
<td align=center><nobr>1.46 GB</nobr></td>
<td align=right><a href=details.php?id=1518337&amp;toseeders=1><font color=#000000>112</font></a></td>
<td align="right">0</td>
<td align="right">49</td><td align=center nowrap><a href=userdetails.php?id=136958>anronn</a></td>
</tr>
<tr>
<td class="torrentCategImg"><a href="browse.php?cat=1"><img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/categs/cat_movie.gif" height="32" alt="Movies"/></a></td>
<td align=left><a href="/details.php?id=1518336">Танцы насмерть [2016 / BDRip] [Action / Sci-Fi / Drama] [3.1/10]</a>
</td>
<td align="right">1</td>
<td align="right"><a href="details.php?id=1518336&amp;page=0#startcomments">11</a></td>
<td align=center width=20><nobr>09-11</nobr></td>
<td align=center><nobr>1.45 GB</nobr></td>
<td align=right><a href=details.php?id=1518336&amp;toseeders=1><font color=#000000>40</font></a></td>
<td align="right">0</td>
<td align="right">10</td><td align=center nowrap><a href=userdetails.php?id=136958>anronn</a></td>
</tr>
</table>
<p align="center"><b>1&nbsp;-&nbsp;100</b> | <a href="browse.php?page=1"><b>101&nbsp;-&nbsp;200</b></a> | <a href="browse.php?page=2"><b>201&nbsp;-&nbsp;300</b></a> | ... | <a href="browse.php?page=5146"><b>514601&nbsp;-&nbsp;514700</b></a> | <a href="browse.php?page=5147"><b>514701&nbsp;-&nbsp;514800</b></a> | <a href="browse.php?page=5148"><b>514801&nbsp;-&nbsp;514863</b></a><br /><b>&lt;&lt;&nbsp;Precedenta</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="browse.php?page=1"><b>Următoarea&nbsp;&gt;&gt;</b></a></p>
</div><p style='color:#F5F4EA;'>0.010104894638062</p>
</div><br/><table class="main footdisclaimer" align=center border=0 cellspacing=0 cellpadding=0><tr><td class=embedded>Schimbul de informație este realizat de către utilizatorii siteului. <strong>Acest site este bazat pe voluntariat, de la utilizatori pentru utilizatori.</strong> Întregul text privind regulile şi condiţiile de utilizare a TORRENTS.MD poate fi găsit <a href=disclamer.php>aici</a>.<br/>

  <div style="font-weight: bold;margin: 10px auto auto;width: 230px;">
    Sharing is caring.
    <img src="https://supernova.zamolxismd.org/m/torrentsmd.eu/pic/smilies/md.gif" style="height: 25px;vertical-align: middle;">
  </div></td></tr></table>
<br/><script type="text/javascript">
  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-2329457-1']);
  _gaq.push(['_trackPageview']);
  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(ga);
  })();
</script></body></html>

'''

finder = BeautifulSoup(data, 'lxml')

table = finder.find('table',{'class':'tableTorrents'})
#a\subset b

#[x for x in r1 if any(y in x for y in b)]
#I = [content for content in table if set(content.contents).issuperset(ALLOWED_TITLE)]
#[[td.text for td in row.find_all("td")] for row in table.find_all("tr")[1:]]


#def experimental_cache(f):
#    l = [('c001name','lastupdated')]
#    @wraps(f)
#    def wrapper(*args, **kwargs):
#        if l ][ l :
#            return f(*args, **kwargs)
#    return wrapper
        
datas = [[td.text for td in row.find_all('td')] for row in table.find_all('tr')]
r = [row for row in table.find_all('tr') if ALLOWED_TITLE.issubset(row.text.split()) ]
#r = [x for x in r if ALLOWED_TITLE.issubset(x.text.split())]

print(datas)
