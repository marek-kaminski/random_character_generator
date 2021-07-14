import random


names = ['Adalbert\n', 'Adalryk\n', 'Ademar\n', 'Adolf\n', 'Albert\n', 'Albrecht\n', 'Alberyk\n', 'Albwin\n', 'Aldmir\n', 'Alfons\n', 'Alfred\n', 'Alodiusz\n', 'Alojzy\n', 'Alwin\n', 'Ansgar\n', 'Ansgary\n', 'Anzelm\n', 'Arbogast\n', 'Arbort\n', 'Armin\n', 'Arnold\n', 'Arnolf\n', 'Arnulf\n', 'Arwid\n', 'Aubert\n', 'Audomar\n', 'Baldomer\n', 'Baldwin\n', 'Beda\n', 'Berard\n', 'Bernard\n', 'Bernardyn\n', 'Bertold\n', 'Bertram\n', 'Berwin\n', 'Bruno\n', 'Brunon\n', 'Burchard\n', 'Dagobert\n', 'Deder\n', 'Dypold\n', 'Dyter\n', 'Detwin\n', 'Edbert\n', 'Edgar\n', 'Edmund\n', 'Edward\n', 'Edwin\n', 'Egbert\n', 'Egon\n', 'Egwin\n', 'Ekhard\n', 'Elpin\n', 'Emeryk\n', 'Erbort\n', 'Ermenfryd\n', 'Ernest\n', 'Erwin\n', 'Eryk\n', 'Ewald\n', 'Ferdynand\n', 'Franciszek\n', 'Franciszek Salezy\n', 'Fryderyk\n', 'Gerald\n', 'Gerard\n', 'Germeriusz\n', 'Gerwazy\n', 'Gerwin\n', 'Ginter\n', 'Gizbert\n', 'Godfryd\n', 'Gotard\n', 'Gumbert\n', 'Guncerz\n', 'Gunter\n', 'Gundolf\n', 'Gustaw\n', 'Gwalbert\n', 'Gwido\n', 'Gwidon\n', 'Harald\n', 'Hekard\n', 'Hekehard\n', 'Helmut\n', 'Henryk\n', 'Herbert\n', 'Herbort\n', 'Hubert\n', 'Herburt\n', 'Herman\n', 'Hermenegild\n', 'Hildebrand\n', 'Hubert\n', 'Hugo\n', 'Hunold\n', 'Igor\n', 'Ildefons\n', 'Ingolf\n', 'Ingwar\n', 'Irmfryd\n', 'Iwo\n', 'Jakert\n', 'Jurand\n', 'Karol\n', 'Konrad\n', 'Konradyn\n', 'Ksawery\n', 'Kanut\n', 'Kutbert\n', 'Lambert\n', 'Leonard\n', 'Leopold\n', 'Lewin\n', 'Lotar\n', 'Lubart\n', 'Ludwik\n', 'Ludwin\n', 'Majnard\n', 'Manfred\n', 'Markwart\n', 'Marold\n', 'Marwald\n', 'Medard\n', 'Norbert\n', 'Norman\n', 'Odo\n', 'Odon\n', 'Odoryk\n', 'Odylon\n', 'Olaf\n', 'Oldmir\n', 'Oleg\n', 'Onold\n', 'Oskar\n', 'Osmund\n', 'Oswald\n', 'Otmar\n', 'Otokar\n', 'Otto\n', 'Pepin\n', 'Rajmund\n', 'Rajner\n', 'Rajnold\n', 'Rambert\n', 'Robert\n', 'Roderyk\n', 'Roger\n', 'Roland\n', 'Romuald\n', 'Rudolf\n', 'Ruprecht\n', 'Ryszard\n', 'Roch\n', 'Switun\n', 'Teobald\n', 'Teodoryk\n', 'Tybald\n', 'Tyter\n', 'Ulryk\n', 'Unold\n', 'Walbert\n', 'Waldebert\n', 'Waldemar\n', 'Walter\n', 'Wigbert\n', 'Wilhelm\n', 'Winand\n', 'Wulstan\n', 'Wulfryk\n', 'Wolfram\n', 'Zybert\n', 'Zygfryd\n', 'Zygmunt\n', 'Zyndram\n', 'Abagor\n', 'Abamon\n', 'Abataly\n', 'Abdaikl\n', 'Abdullah (name)\n', 'Abel \n', 'Abelyar\n', 'Abid\n', 'Abily\n', 'Abnody\n', 'Abo (name)\n', 'Abram (name)\n', 'Aburom\n', 'Adam \n', 'Afanasy\n', 'Agafangel\n', 'Agafodor\n', 'Agafon\n', 'Agafonik\n', 'Agafopod\n', 'Anatoly\n', 'Andrey\n', 'Anton \n', 'Arkadiy\n', 'Arkady\n', 'Artemy\n', 'Artyom\n', 'Avda \n', 'Avdakt\n', 'Avdelay\n', 'Avdey\n', 'Avdifaks\n', 'Avdiky\n', 'Avdiyes\n', 'Avdon \n', 'Avel\n', 'Avenir \n', 'Aventin \n', 'Averky\n', 'Avgar\n', 'Avgury\n', 'Avgust\n', 'Avgustin\n', 'Avian \n', 'Avim \n', 'Avimelekh\n', 'Avip\n', 'Avit\n', 'Aviv\n', 'Avksenty\n', 'Avksily\n', 'Avksivy\n', 'Avkt\n', 'Avram \n', 'Avrelian\n', 'Avrely\n', 'Avrey\n', 'Avros\n', 'Avsey\n', 'olaf\n', 'Avtonom\n', 'Avudim\n', 'Avundy\n', 'Avva\n', 'Avvakir\n', 'Avvakum \n', 'Bogdan\n', 'Boris \n', 'Borislav\n', 'Boyan \n', 'Budimir\n', 'Damir\n', 'Daniel\n', 'Daniil\n', 'Darko \n', 'David (name)\n', 'Dmitry\n', 'Eduard (name)\n', 'Elmir\n', 'Fedot\n', 'Fyodor\n', 'Gennady\n', 'Genrikh\n', 'Georgy \n', 'Gerasim\n', 'Gleb\n', 'Goran (Slavic name)\n', 'Gordan\n', 'Grigory\n', 'Grischa\n', 'Ignat\n', 'Ilarion\n', 'Ilya\n', 'Irek \n', 'Ivan (name)\n', 'Jaroslav\n', 'Joakim\n', 'Joseph\n', 'Kirill\n', 'Kliment\n', 'Kolya (disambiguation)\n', 'Konstantin\n', 'Lavrentiy\n', 'Leon \n', 'Leonid\n', 'Luca \n', 'Lukyan\n', 'Magomedkhan\n', 'Matvei\n', 'Maxim \n', 'Mikhail\n', 'Milan \n', 'Milorad\n', 'Miroslav \n', 'Misha (disambiguation)\n', 'Mstislav \n', 'Nail \n', 'Nectarios\n', 'Nikita \n', 'Nikola\n', 'Nikolay\n', 'Oleg\n', 'Osip\n', 'Ossip\n', 'Panteleimon\n', 'Pavel\n', 'Pavsikakiy\n', 'Piotr\n', 'Prokhor\n', 'Prokopy\n', 'Pyotr\n', 'Radomir\n', 'Radovan\n', 'Ratimir\n', 'Rodion\n', 'Roman \n', 'Rostislav \n', 'Ruslan \n', 'Rustem\n', 'Sasha (name)\n', 'Simeon\n', 'Simon \n', 'Slava (disambiguation)\n', 'Stanislav \n', 'Stepan \n', 'Svetoslav\n', 'Sviatoslav\n', 'Taras (name)\n', 'Timofey\n', 'Vadim\n', 'Valentin\n', 'Valery\n', 'Vasily\n', 'Veniamin\n', 'Victor (name)\n', 'Vladimir (name)\n', 'Vladislav\n', 'Vsevolod\n', 'Vuk (name)\n', 'Yakov\n', 'Yaroslav\n', 'Yefim\n', 'Yegor\n', 'Yermolay\n', 'Yevgeny\n', 'Yury\n', 'Zakhar\n', 'Zinoviy\n', 'Zinovy\n']
nouns = ['Ability\n', 'Access\n', 'Accident\n', 'Account\n', 'Act\n', 'Action\n', 'Activity\n', 'Actor\n', 'Ad\n', 'Addition\n', 'Address\n', 'Administration\n', 'Advantage\n', 'Advertising\n', 'Advice\n', 'Affair\n', 'Age\n', 'Agency\n', 'Agreement\n', 'Air\n', 'Airport\n', 'Alcohol\n', 'Ambition\n', 'Amount\n', 'Analysis\n', 'Analyst\n', 'Animal\n', 'Answer\n', 'Anxiety\n', 'Apartment\n', 'Appearance\n', 'Apple\n', 'Application\n', 'Appointment\n', 'Area\n', 'Argument\n', 'Army\n', 'Arrival\n', 'Art\n', 'Article\n', 'Aspect\n', 'Assignment\n', 'Assistance\n', 'Assistant\n', 'Association\n', 'Assumption\n', 'Atmosphere\n', 'Attempt\n', 'Attention\n', 'Attitude\n', 'Audience\n', 'Aunt\n', 'Average\n', 'Awareness\n', 'Back\n', 'Bad\n', 'Balance\n', 'Ball\n', 'Bank\n', 'Baseball\n', 'Basis\n', 'Basket\n', 'Bath\n', 'Bathroom\n', 'Bedroom\n', 'Beer\n', 'Beginning\n', 'Benefit\n', 'Bird\n', 'Birth\n', 'Birthday\n', 'Bit\n', 'Blood\n', 'Board\n', 'Boat\n', 'Body\n', 'Bonus\n', 'Book\n', 'people\n', 'history\n', 'way\n', 'art\n', 'world\n', 'information\n', 'map\n', 'two\n', 'family\n', 'government\n', 'health\n', 'system\n', 'computer\n', 'meat\n', 'year\n', 'thanks\n', 'music\n', 'person\n', 'reading\n', 'method\n', 'data\n', 'food\n', 'understanding\n', 'theory\n', 'law\n', 'bird\n', 'literature\n', 'problem\n', 'software\n', 'control\n', 'knowledge\n', 'power\n', 'ability\n', 'economics\n', 'love\n', 'internet\n', 'television\n', 'science\n', 'library\n', 'nature\n', 'fact\n', 'product\n', 'idea\n', 'temperature\n', 'investment\n', 'area\n', 'society\n', 'activity\n', 'story\n', 'industry\n', 'media\n', 'thing\n', 'oven\n', 'community\n', 'definition\n', 'safety\n', 'quality\n', 'development\n', 'language\n', 'management\n', 'player\n', 'variety\n', 'video\n', 'week\n', 'security\n', 'country\n', 'exam\n', 'movie\n', 'organization\n', 'equipment\n', 'physics\n', 'analysis\n', 'policy\n', 'series\n', 'thought\n', 'basis\n', 'boyfriend\n', 'direction\n', 'strategy\n', 'technology\n', 'army\n', 'camera\n', 'freedom\n', 'paper\n', 'environment\n', 'child\n', 'instance\n', 'month\n', 'truth\n', 'marketing\n', 'university\n', 'writing\n', 'article\n', 'department\n', 'difference\n', 'goal\n', 'news\n', 'audience\n', 'fishing\n', 'growth\n', 'income\n', 'marriage\n', 'user\n', 'combination\n', 'failure\n', 'meaning\n', 'medicine\n', 'philosophy\n', 'teacher\n', 'communication\n', 'night\n', 'chemistry\n', 'disease\n', 'disk\n', 'energy\n', 'nation\n', 'road\n', 'role\n', 'soup\n', 'advertising\n', 'location\n', 'success\n', 'addition\n', 'apartment\n', 'education\n', 'math\n', 'moment\n', 'painting\n', 'politics\n', 'attention\n', 'decision\n', 'event\n', 'property\n', 'shopping\n', 'student\n', 'wood\n', 'competition\n', 'distribution\n', 'entertainment\n', 'office\n', 'population\n', 'president\n', 'unit\n', 'category\n', 'cigarette\n', 'context\n', 'introduction\n', 'opportunity\n', 'performance\n', 'driver\n', 'flight\n', 'length\n', 'magazine\n', 'newspaper\n', 'relationship\n', 'teaching\n', 'cell\n', 'dealer\n', 'finding\n', 'lake\n', 'member\n', 'message\n', 'phone\n', 'scene\n', 'appearance\n', 'association\n', 'concept\n', 'customer\n', 'death\n', 'discussion\n', 'housing\n', 'inflation\n', 'insurance\n', 'mood\n', 'woman\n', 'advice\n', 'blood\n', 'effort\n', 'expression\n', 'importance\n', 'opinion\n', 'payment\n', 'reality\n', 'responsibility\n', 'situation\n', 'skill\n', 'statement\n', 'wealth\n', 'application\n', 'city\n', 'county\n', 'depth\n', 'estate\n', 'foundation\n', 'grandmother\n', 'heart\n', 'perspective\n', 'photo\n', 'recipe\n', 'studio\n', 'topic\n', 'collection\n', 'depression\n', 'imagination\n', 'passion\n', 'percentage\n', 'resource\n', 'setting\n', 'ad\n', 'agency\n', 'college\n', 'connection\n', 'criticism\n', 'debt\n', 'description\n', 'memory\n', 'patience\n', 'secretary\n', 'solution\n', 'administration\n', 'aspect\n', 'attitude\n', 'director\n', 'personality\n', 'psychology\n', 'recommendation\n', 'response\n', 'selection\n', 'storage\n', 'version\n', 'alcohol\n', 'argument\n', 'complaint\n', 'contract\n', 'emphasis\n', 'highway\n', 'loss\n', 'membership\n', 'possession\n', 'preparation\n', 'steak\n', 'union\n', 'agreement\n', 'cancer\n', 'currency\n', 'employment\n', 'engineering\n', 'entry\n', 'interaction\n', 'mixture\n', 'preference\n', 'region\n', 'republic\n', 'tradition\n', 'virus\n', 'actor\n', 'classroom\n', 'delivery\n', 'device\n', 'difficulty\n', 'drama\n', 'election\n', 'engine\n', 'football\n', 'guidance\n', 'hotel\n', 'owner\n', 'priority\n', 'protection\n', 'suggestion\n', 'tension\n', 'variation\n', 'anxiety\n', 'atmosphere\n', 'awareness\n', 'bath\n', 'bread\n', 'candidate\n', 'climate\n', 'comparison\n', 'confusion\n', 'construction\n', 'elevator\n', 'emotion\n', 'employee\n', 'employer\n', 'guest\n', 'height\n', 'leadership\n', 'mall\n', 'manager\n', 'operation\n', 'recording\n', 'sample\n', 'transportation\n', 'charity\n', 'cousin\n', 'disaster\n', 'editor\n', 'efficiency\n', 'excitement\n', 'extent\n', 'feedback\n', 'guitar\n', 'homework\n', 'leader\n', 'mom\n', 'outcome\n', 'permission\n', 'presentation\n', 'promotion\n', 'reflection\n', 'refrigerator\n', 'resolution\n', 'revenue\n', 'session\n', 'singer\n', 'tennis\n', 'basket\n', 'bonus\n', 'cabinet\n', 'childhood\n', 'church\n', 'clothes\n', 'coffee\n', 'dinner\n', 'drawing\n', 'hair\n', 'hearing\n', 'initiative\n', 'judgment\n', 'lab\n', 'measurement\n', 'mode\n', 'mud\n', 'orange\n', 'poetry\n', 'police\n', 'possibility\n', 'procedure\n', 'queen\n', 'ratio\n', 'relation\n', 'restaurant\n', 'satisfaction\n', 'sector\n', 'signature\n', 'significance\n', 'song\n', 'tooth\n', 'town\n', 'vehicle\n', 'volume\n', 'wife\n', 'accident\n', 'airport\n', 'appointment\n', 'arrival\n', 'assumption\n', 'baseball\n', 'chapter\n', 'committee\n', 'conversation\n', 'database\n', 'enthusiasm\n', 'error\n', 'explanation\n', 'farmer\n', 'gate\n', 'girl\n', 'hall\n', 'historian\n', 'hospital\n', 'injury\n', 'instruction\n', 'maintenance\n', 'manufacturer\n', 'meal\n', 'perception\n', 'pie\n', 'poem\n', 'presence\n', 'proposal\n', 'reception\n', 'replacement\n', 'revolution\n', 'river\n', 'son\n', 'speech\n', 'tea\n', 'village\n', 'warning\n', 'winner\n', 'worker\n', 'writer\n', 'assistance\n', 'breath\n', 'buyer\n', 'chest\n', 'chocolate\n', 'conclusion\n', 'contribution\n', 'cookie\n', 'courage\n', 'dad\n', 'desk\n', 'drawer\n', 'establishment\n', 'examination\n', 'garbage\n', 'grocery\n', 'honey\n', 'impression\n', 'improvement\n', 'independence\n', 'insect\n', 'inspection\n', 'inspector\n', 'king\n', 'ladder\n', 'menu\n', 'penalty\n', 'piano\n', 'potato\n', 'profession\n', 'professor\n', 'quantity\n', 'reaction\n', 'requirement\n', 'salad\n', 'sister\n', 'supermarket\n', 'tongue\n', 'weakness\n', 'wedding\n', 'affair\n', 'ambition\n', 'analyst\n', 'apple\n', 'assignment\n', 'assistant\n', 'bathroom\n', 'bedroom\n', 'beer\n', 'birthday\n', 'celebration\n', 'championship\n', 'cheek\n', 'client\n', 'consequence\n', 'departure\n', 'diamond\n', 'dirt\n', 'ear\n', 'fortune\n', 'friendship\n', 'funeral\n', 'gene\n', 'girlfriend\n', 'hat\n', 'indication\n', 'intention\n', 'lady\n', 'midnight\n', 'negotiation\n', 'obligation\n', 'passenger\n', 'pizza\n', 'platform\n', 'poet\n', 'pollution\n', 'recognition\n', 'reputation\n', 'shirt\n', 'sir\n', 'speaker\n', 'stranger\n', 'surgery\n', 'sympathy\n', 'tale\n', 'throat\n', 'trainer\n', 'uncle\n', 'youth\n', 'time\n', 'work\n', 'film\n', 'water\n', 'money\n', 'example\n', 'while\n', 'business\n', 'study\n', 'game\n', 'life\n', 'form\n', 'air\n', 'day\n', 'place\n', 'number\n', 'part\n', 'field\n', 'fish\n', 'back\n', 'process\n', 'heat\n', 'hand\n', 'experience\n', 'job\n', 'book\n', 'end\n', 'point\n', 'type\n', 'home\n', 'economy\n', 'value\n', 'body\n', 'market\n', 'guide\n', 'interest\n', 'state\n', 'radio\n', 'course\n', 'company\n', 'price\n', 'size\n', 'card\n', 'list\n', 'mind\n', 'trade\n', 'line\n', 'care\n', 'group\n', 'risk\n', 'word\n', 'fat\n', 'force\n', 'key\n', 'light\n', 'training\n', 'name\n', 'school\n', 'top\n', 'amount\n', 'level\n', 'order\n', 'practice\n', 'research\n', 'sense\n', 'service\n', 'piece\n', 'web\n', 'boss\n', 'sport\n', 'fun\n', 'house\n', 'page\n', 'term\n', 'test\n', 'answer\n', 'sound\n', 'focus\n', 'matter\n', 'kind\n', 'soil\n', 'board\n', 'oil\n', 'picture\n', 'access\n', 'garden\n', 'range\n', 'rate\n', 'reason\n', 'future\n', 'site\n', 'demand\n', 'exercise\n', 'image\n', 'case\n', 'cause\n', 'coast\n', 'action\n', 'age\n', 'bad\n', 'boat\n', 'record\n', 'result\n', 'section\n', 'building\n', 'mouse\n', 'cash\n', 'class\n', 'nothing\n', 'period\n', 'plan\n', 'store\n', 'tax\n', 'side\n', 'subject\n', 'space\n', 'rule\n', 'stock\n', 'weather\n', 'chance\n', 'figure\n', 'man\n', 'model\n', 'source\n', 'beginning\n', 'earth\n', 'program\n', 'chicken\n', 'design\n', 'feature\n', 'head\n', 'material\n', 'purpose\n', 'question\n', 'rock\n', 'salt\n', 'act\n', 'birth\n', 'car\n', 'dog\n', 'object\n', 'scale\n', 'sun\n', 'note\n', 'profit\n', 'rent\n', 'speed\n', 'style\n', 'war\n', 'bank\n', 'craft\n', 'half\n', 'inside\n', 'outside\n', 'standard\n', 'bus\n', 'exchange\n', 'eye\n', 'fire\n', 'position\n', 'pressure\n', 'stress\n', 'advantage\n', 'benefit\n', 'box\n', 'frame\n', 'issue\n', 'step\n', 'cycle\n', 'face\n', 'item\n', 'metal\n', 'paint\n', 'review\n', 'room\n', 'screen\n', 'structure\n', 'view\n', 'account\n', 'ball\n', 'discipline\n', 'medium\n', 'share\n', 'balance\n', 'bit\n', 'black\n', 'bottom\n', 'choice\n', 'gift\n', 'impact\n', 'machine\n', 'shape\n', 'tool\n', 'wind\n', 'address\n', 'average\n', 'career\n', 'culture\n', 'morning\n', 'pot\n', 'sign\n', 'table\n', 'task\n', 'condition\n', 'contact\n', 'credit\n', 'egg\n', 'hope\n', 'ice\n', 'network\n', 'north\n', 'square\n', 'attempt\n', 'date\n', 'effect\n', 'link\n', 'post\n', 'star\n', 'voice\n', 'capital\n', 'challenge\n', 'friend\n', 'self\n', 'shot\n', 'brush\n', 'couple\n', 'debate\n', 'exit\n', 'front\n', 'function\n', 'lack\n', 'living\n', 'plant\n', 'plastic\n', 'spot\n', 'summer\n', 'taste\n', 'theme\n', 'track\n', 'wing\n', 'brain\n', 'button\n', 'click\n', 'desire\n', 'foot\n', 'gas\n', 'influence\n', 'notice\n', 'rain\n', 'wall\n', 'base\n', 'damage\n', 'distance\n', 'feeling\n', 'pair\n', 'savings\n', 'staff\n', 'sugar\n', 'target\n', 'text\n', 'animal\n', 'author\n', 'budget\n', 'discount\n', 'file\n', 'ground\n', 'lesson\n', 'minute\n', 'officer\n', 'phase\n', 'reference\n', 'register\n', 'sky\n', 'stage\n', 'stick\n', 'title\n', 'trouble\n', 'bowl\n', 'bridge\n', 'campaign\n', 'character\n', 'club\n', 'edge\n', 'evidence\n', 'fan\n', 'letter\n', 'lock\n', 'maximum\n', 'novel\n', 'option\n', 'pack\n', 'park\n', 'plenty\n', 'quarter\n', 'skin\n', 'sort\n', 'weight\n', 'baby\n', 'background\n', 'carry\n', 'dish\n', 'factor\n', 'fruit\n', 'glass\n', 'joint\n', 'master\n', 'muscle\n', 'red\n', 'strength\n', 'traffic\n', 'trip\n', 'vegetable\n', 'appeal\n', 'chart\n', 'gear\n', 'ideal\n', 'kitchen\n', 'land\n', 'log\n', 'mother\n', 'net\n', 'party\n', 'principle\n', 'relative\n', 'sale\n', 'season\n', 'signal\n', 'spirit\n', 'street\n', 'tree\n', 'wave\n', 'belt\n', 'bench\n', 'commission\n', 'copy\n', 'drop\n', 'minimum\n', 'path\n', 'progress\n', 'project\n', 'sea\n', 'south\n', 'status\n', 'stuff\n', 'ticket\n', 'tour\n', 'angle\n', 'blue\n', 'breakfast\n', 'confidence\n', 'daughter\n', 'degree\n', 'doctor\n', 'dot\n', 'dream\n', 'duty\n', 'essay\n', 'father\n', 'fee\n', 'finance\n', 'hour\n', 'juice\n', 'limit\n', 'luck\n', 'milk\n', 'mouth\n', 'peace\n', 'pipe\n', 'seat\n', 'stable\n', 'storm\n', 'substance\n', 'team\n', 'trick\n', 'afternoon\n', 'bat\n', 'beach\n', 'blank\n', 'catch\n', 'chain\n', 'consideration\n', 'cream\n', 'crew\n', 'detail\n', 'gold\n', 'interview\n', 'kid\n', 'mark\n', 'match\n', 'mission\n', 'pain\n', 'pleasure\n', 'score\n', 'screw\n', 'sex\n', 'shop\n', 'shower\n', 'suit\n', 'tone\n', 'window\n', 'agent\n', 'band\n', 'block\n', 'bone\n', 'calendar\n', 'cap\n', 'coat\n', 'contest\n', 'corner\n', 'court\n', 'cup\n', 'district\n', 'door\n', 'east\n', 'finger\n', 'garage\n', 'guarantee\n', 'hole\n', 'hook\n', 'implement\n', 'layer\n', 'lecture\n', 'lie\n', 'manner\n', 'meeting\n', 'nose\n', 'parking\n', 'partner\n', 'profile\n', 'respect\n', 'rice\n', 'routine\n', 'schedule\n', 'swimming\n', 'telephone\n', 'tip\n', 'winter\n', 'airline\n', 'bag\n', 'battle\n', 'bed\n', 'bill\n', 'bother\n', 'cake\n', 'code\n', 'curve\n', 'designer\n', 'dimension\n', 'dress\n', 'ease\n', 'emergency\n', 'evening\n', 'extension\n', 'farm\n', 'fight\n', 'gap\n', 'grade\n', 'holiday\n', 'horror\n', 'horse\n', 'host\n', 'husband\n', 'loan\n', 'mistake\n', 'mountain\n', 'nail\n', 'noise\n', 'occasion\n', 'package\n', 'patient\n', 'pause\n', 'phrase\n', 'proof\n', 'race\n', 'relief\n', 'sand\n', 'sentence\n', 'shoulder\n', 'smoke\n', 'stomach\n', 'string\n', 'tourist\n', 'towel\n', 'vacation\n', 'west\n', 'wheel\n', 'wine\n', 'arm\n', 'aside\n', 'associate\n', 'bet\n', 'blow\n', 'border\n', 'branch\n', 'breast\n', 'brother\n', 'buddy\n', 'bunch\n', 'chip\n', 'coach\n', 'cross\n', 'document\n', 'draft\n', 'dust\n', 'expert\n', 'floor\n', 'god\n', 'golf\n', 'habit\n', 'iron\n', 'judge\n', 'knife\n', 'landscape\n', 'league\n', 'mail\n', 'mess\n', 'native\n', 'opening\n', 'parent\n', 'pattern\n', 'pin\n', 'pool\n', 'pound\n', 'request\n', 'salary\n', 'shame\n', 'shelter\n', 'shoe\n', 'silver\n', 'tackle\n', 'tank\n', 'trust\n', 'assist\n', 'bake\n', 'bar\n', 'bell\n', 'bike\n', 'blame\n', 'boy\n', 'brick\n', 'chair\n', 'closet\n', 'clue\n', 'collar\n', 'comment\n', 'conference\n', 'devil\n', 'diet\n', 'fear\n', 'fuel\n', 'glove\n', 'jacket\n', 'lunch\n', 'monitor\n', 'mortgage\n', 'nurse\n', 'pace\n', 'panic\n', 'peak\n', 'plane\n', 'reward\n', 'row\n', 'sandwich\n', 'shock\n', 'spite\n', 'spray\n', 'surprise\n', 'till\n', 'transition\n', 'weekend\n', 'welcome\n', 'yard\n', 'alarm\n', 'bend\n', 'bicycle\n', 'bite\n', 'blind\n', 'bottle\n', 'cable\n', 'candle\n', 'clerk\n', 'cloud\n', 'concert\n', 'counter\n', 'flower\n', 'grandfather\n', 'harm\n', 'knee\n', 'lawyer\n', 'leather\n', 'load\n', 'mirror\n', 'neck\n', 'pension\n', 'plate\n', 'purple\n', 'ruin\n', 'ship\n', 'skirt\n', 'slice\n', 'snow\n', 'specialist\n', 'stroke\n', 'switch\n', 'trash\n', 'tune\n', 'zone\n', 'anger\n', 'award\n', 'bid\n', 'bitter\n', 'boot\n', 'bug\n', 'camp\n', 'candy\n', 'carpet\n', 'cat\n', 'champion\n', 'channel\n', 'clock\n', 'comfort\n', 'cow\n', 'crack\n', 'engineer\n', 'entrance\n', 'fault\n', 'grass\n', 'guy\n', 'hell\n', 'highlight\n', 'incident\n', 'island\n', 'joke\n', 'jury\n', 'leg\n', 'lip\n', 'mate\n', 'motor\n', 'nerve\n', 'passage\n', 'pen\n', 'pride\n', 'priest\n', 'prize\n', 'promise\n', 'resident\n', 'resort\n', 'ring\n', 'roof\n', 'rope\n', 'sail\n', 'scheme\n', 'script\n', 'sock\n', 'station\n', 'toe\n', 'tower\n', 'truck\n', 'witness\n', 'a\n', 'you\n', 'it\n', 'can\n', 'will\n', 'if\n', 'one\n', 'many\n', 'most\n', 'other\n', 'use\n', 'make\n', 'good\n', 'look\n', 'help\n', 'go\n', 'great\n', 'being\n', 'few\n', 'might\n', 'still\n', 'public\n', 'read\n', 'keep\n', 'start\n', 'give\n', 'human\n', 'local\n', 'general\n', 'she\n', 'specific\n', 'long\n', 'play\n', 'feel\n', 'high\n', 'tonight\n', 'put\n', 'common\n', 'set\n', 'change\n', 'simple\n', 'past\n', 'big\n', 'possible\n', 'particular\n', 'today\n', 'major\n', 'personal\n', 'current\n', 'national\n', 'cut\n', 'natural\n', 'physical\n', 'show\n', 'try\n', 'check\n', 'second\n', 'call\n', 'move\n', 'pay\n', 'let\n', 'increase\n', 'single\n', 'individual\n', 'turn\n', 'ask\n', 'buy\n', 'guard\n', 'hold\n', 'main\n', 'offer\n', 'potential\n', 'professional\n', 'international\n', 'travel\n', 'cook\n', 'alternative\n', 'following\n', 'special\n', 'working\n', 'whole\n', 'dance\n', 'excuse\n', 'cold\n', 'commercial\n', 'low\n', 'purchase\n', 'deal\n', 'primary\n', 'worth\n', 'fall\n', 'necessary\n', 'positive\n', 'produce\n', 'search\n', 'present\n', 'spend\n', 'talk\n', 'creative\n', 'tell\n', 'cost\n', 'drive\n', 'green\n', 'support\n', 'glad\n', 'remove\n', 'return\n', 'run\n', 'complex\n', 'due\n', 'effective\n', 'middle\n', 'regular\n', 'reserve\n', 'independent\n', 'leave\n', 'original\n', 'reach\n', 'rest\n', 'serve\n', 'watch\n', 'beautiful\n', 'charge\n', 'active\n', 'break\n', 'negative\n', 'safe\n', 'stay\n', 'visit\n', 'visual\n', 'affect\n', 'cover\n', 'report\n', 'rise\n', 'walk\n', 'white\n', 'beyond\n', 'junior\n', 'pick\n', 'unique\n', 'anything\n', 'classic\n', 'final\n', 'lift\n', 'mix\n', 'private\n', 'stop\n', 'teach\n', 'western\n', 'concern\n', 'familiar\n', 'fly\n', 'official\n', 'broad\n', 'comfortable\n', 'gain\n', 'maybe\n', 'rich\n', 'save\n', 'stand\n', 'young\n', 'fail\n', 'heavy\n', 'hello\n', 'lead\n', 'listen\n', 'valuable\n', 'worry\n', 'handle\n', 'leading\n', 'meet\n', 'release\n', 'sell\n', 'finish\n', 'normal\n', 'press\n', 'ride\n', 'secret\n', 'spread\n', 'spring\n', 'tough\n', 'wait\n', 'brown\n', 'deep\n', 'display\n', 'flow\n', 'hit\n', 'objective\n', 'shoot\n', 'touch\n', 'cancel\n', 'chemical\n', 'cry\n', 'dump\n', 'extreme\n', 'push\n', 'conflict\n', 'eat\n', 'fill\n', 'formal\n', 'jump\n', 'kick\n', 'opposite\n', 'pass\n', 'pitch\n', 'remote\n', 'total\n', 'treat\n', 'vast\n', 'abuse\n', 'beat\n', 'burn\n', 'deposit\n', 'print\n', 'raise\n', 'sleep\n', 'somewhere\n', 'advance\n', 'anywhere\n', 'consist\n', 'dark\n', 'double\n', 'draw\n', 'equal\n', 'fix\n', 'hire\n', 'internal\n', 'join\n', 'kill\n', 'sensitive\n', 'tap\n', 'win\n', 'attack\n', 'claim\n', 'constant\n', 'drag\n', 'drink\n', 'guess\n', 'minor\n', 'pull\n', 'raw\n', 'soft\n', 'solid\n', 'wear\n', 'weird\n', 'wonder\n', 'annual\n', 'count\n', 'dead\n', 'doubt\n', 'feed\n', 'forever\n', 'impress\n', 'nobody\n', 'repeat\n', 'round\n', 'sing\n', 'slide\n', 'strip\n', 'whereas\n', 'wish\n', 'combine\n', 'command\n', 'dig\n', 'divide\n', 'equivalent\n', 'hang\n', 'hunt\n', 'initial\n', 'march\n', 'mention\n', 'smell\n', 'spiritual\n', 'survey\n', 'tie\n', 'adult\n', 'brief\n', 'crazy\n', 'escape\n', 'gather\n', 'hate\n', 'prior\n', 'repair\n', 'rough\n', 'sad\n', 'scratch\n', 'sick\n', 'strike\n', 'employ\n', 'external\n', 'hurt\n', 'illegal\n', 'laugh\n', 'lay\n', 'mobile\n', 'nasty\n', 'ordinary\n', 'respond\n', 'royal\n', 'senior\n', 'split\n', 'strain\n', 'struggle\n', 'swim\n', 'train\n', 'upper\n', 'wash\n', 'yellow\n', 'convert\n', 'crash\n', 'dependent\n', 'fold\n', 'funny\n', 'grab\n', 'hide\n', 'miss\n', 'permit\n', 'quote\n', 'recover\n', 'resolve\n', 'roll\n', 'sink\n', 'slip\n', 'spare\n', 'suspect\n', 'sweet\n', 'swing\n', 'twist\n', 'upstairs\n', 'usual\n', 'abroad\n', 'brave\n', 'calm\n', 'concentrate\n', 'estimate\n', 'grand\n', 'male\n', 'mine\n', 'prompt\n', 'quiet\n', 'refuse\n', 'regret\n', 'reveal\n', 'rush\n', 'shake\n', 'shift\n', 'shine\n', 'steal\n', 'suck\n', 'surround\n', 'anybody\n', 'bear\n', 'brilliant\n', 'dare\n', 'dear\n', 'delay\n', 'drunk\n', 'female\n', 'hurry\n', 'inevitable\n', 'invite\n', 'kiss\n', 'neat\n', 'pop\n', 'punch\n', 'quit\n', 'reply\n', 'representative\n', 'resist\n', 'rip\n', 'rub\n', 'silly\n', 'smile\n', 'spell\n', 'stretch\n', 'stupid\n', 'tear\n', 'temporary\n', 'tomorrow\n', 'wake\n', 'wrap\n', 'Boss\n', 'Bottom\n', 'Box\n', 'Boy\n', 'Boyfriend\n', 'Bread\n', 'Breath\n', 'Brother\n', 'Building\n', 'Bus\n', 'Business\n', 'Buyer\n', 'Cabinet\n', 'Camera\n', 'Cancer\n', 'Candidate\n', 'Capital\n', 'Car\n', 'Card\n', 'Care\n', 'Career\n', 'Case\n', 'Cash\n', 'Cat\n', 'Category\n', 'Cause\n', 'Celebration\n', 'Cell\n', 'Championship\n', 'Chance\n', 'Chapter\n', 'Charity\n', 'Cheek\n', 'Chemistry\n', 'Chest\n', 'Chicken\n', 'Child\n', 'Childhood\n', 'Chocolate\n', 'Choice\n', 'Church\n', 'Cigarette\n', 'City\n', 'Class\n', 'Classroom\n', 'Client\n', 'Climate\n', 'Clothes\n', 'Coast\n', 'Coffee\n', 'Collection\n', 'College\n', 'Combination\n', 'Committee\n', 'Communication\n', 'Community\n', 'Company\n', 'Comparison\n', 'Competition\n', 'Complaint\n', 'Computer\n', 'Concept\n', 'Conclusion\n', 'Condition\n', 'Confusion\n', 'Connection\n', 'Consequence\n', 'Construction\n', 'Contact\n', 'Context\n', 'Contract\n', 'Contribution\n', 'Control\n', 'Conversation\n', 'Cookie\n', 'Country\n', 'County\n', 'Courage\n', 'Course\n', 'Cousin\n', 'Craft\n', 'Credit\n', 'Criticism\n', 'Culture\n', 'Currency\n', 'Customer\n', 'Cycle\n', 'Dad\n', 'Data\n', 'Database\n', 'Date\n', 'Day\n', 'Dealer\n', 'Death\n', 'Debt\n', 'Decision\n', 'Definition\n', 'Delivery\n', 'Demand\n', 'Department\n', 'Departure\n', 'Depression\n', 'Depth\n', 'Description\n', 'Design\n', 'Desk\n', 'Development\n', 'Device\n', 'Diamond\n', 'Difference\n', 'Difficulty\n', 'Dinner\n', 'Direction\n', 'Director\n', 'Dirt\n', 'Disaster\n', 'Discipline\n', 'Discussion\n', 'Disease\n', 'Disk\n', 'Distribution\n', 'Dog\n', 'Drama\n', 'Drawer\n', 'Drawing\n', 'Driver\n', 'Ear\n', 'Earth\n', 'Economics\n', 'Economy\n', 'Editor\n', 'Education\n', 'Effect\n', 'Efficiency\n', 'Effort\n', 'Egg\n', 'Election\n', 'Elevator\n', 'Emotion\n', 'Emphasis\n', 'Employee\n', 'Employer\n', 'Employment\n', 'End\n', 'Energy\n', 'Engine\n', 'Entertainment\n', 'Enthusiasm\n', 'Entry\n', 'Environment\n', 'Equipment\n', 'Error\n', 'Establishment\n', 'Estate\n', 'Event\n', 'Exam\n', 'Examination\n', 'Example\n', 'Exchange\n', 'Excitement\n', 'Exercise\n', 'Experience\n', 'Explanation\n', 'Expression\n', 'Extent\n', 'Eye\n', 'Face\n', 'Fact\n', 'Failure\n', 'Family\n', 'Farmer\n', 'Fat\n', 'Feature\n', 'Feedback\n', 'Field\n', 'Figure\n', 'Film\n', 'Finding\n', 'Fire\n', 'Fish\n', 'Flight\n', 'Focus\n', 'Food\n', 'Football\n', 'Force\n', 'Form\n', 'Fortune\n', 'Foundation\n', 'Frame\n', 'Freedom\n', 'Friendship\n', 'Fun\n', 'Funeral\n', 'Future\n', 'Game\n', 'Garbage\n', 'Garden\n', 'Gate\n', 'Gene\n', 'Gift\n', 'Girl\n', 'Girlfriend\n', 'Goal\n', 'Government\n', 'Grandmother\n', 'Grocery\n', 'gun\n', 'Group\n', 'Growth\n', 'Guest\n', 'Guidance\n', 'Guide\n', 'Guitar\n', 'Hair\n', 'Half\n', 'Hall\n', 'Hand\n', 'Hat\n', 'Head\n', 'Health\n', 'Hearing\n', 'Heart\n', 'Heat\n', 'Height\n', 'Highway\n', 'Historian\n', 'History\n', 'Home\n', 'Homework\n', 'Honey\n', 'Hope\n', 'Hospital\n', 'Hotel\n', 'House\n', 'Housing\n', 'Ice\n', 'Idea\n', 'Image\n', 'Imagination\n', 'Impact\n', 'Importance\n', 'Impression\n', 'Improvement\n', 'Income\n', 'Independence\n', 'Indication\n', 'Industry\n', 'Inflation\n', 'Information\n', 'Initiative\n', 'Injury\n', 'Insect\n', 'Inside\n', 'Inspection\n', 'Inspector\n', 'Instance\n', 'Instruction\n', 'Insurance\n', 'Intention\n', 'Interaction\n', 'Interest\n', 'Internet\n', 'Introduction\n', 'Investment\n', 'Issue\n', 'Item\n', 'Job\n', 'Judgment\n', 'Key\n', 'Kind\n', 'King\n', 'Knowledge\n', 'Lab\n', 'Ladder\n', 'Lady\n', 'Lake\n', 'Language\n', 'Law\n', 'Leader\n', 'Leadership\n', 'Length\n', 'Level\n', 'Library\n', 'Life\n', 'Light\n', 'Line\n', 'Link\n', 'List\n', 'Literature\n', 'Location\n', 'Loss\n', 'Love\n', 'Machine\n', 'Magazine\n', 'Maintenance\n', 'Mall\n', 'Man\n', 'Management\n', 'Manager\n', 'Manufacturer\n', 'Map\n', 'Market\n', 'Marketing\n', 'Marriage\n', 'Material\n', 'Math\n', 'Matter\n', 'Meal\n', 'Meaning\n', 'Measurement\n', 'Meat\n', 'Media\n', 'Medicine\n', 'Medium\n', 'Member\n', 'Membership\n', 'Memory\n', 'Menu\n', 'Message\n', 'Metal\n', 'Method\n', 'Midnight\n', 'Mind\n', 'Mixture\n', 'Mode\n', 'Model\n', 'Mom\n', 'Moment\n', 'Money\n', 'Month\n', 'Mood\n', 'Morning\n', 'Mouse\n', 'Movie\n', 'Mud\n', 'Music\n', 'Name\n', 'Nation\n', 'Nature\n', 'Negotiation\n', 'Network\n', 'News\n', 'Newspaper\n', 'Night\n', 'Note\n', 'Nothing\n', 'Number\n', 'Object\n', 'Obligation\n', 'Office\n', 'Oil\n', 'Operation\n', 'Opinion\n', 'Opportunity\n', 'Orange\n', 'Order\n', 'Organization\n', 'Outcome\n', 'Outside\n', 'Oven\n', 'Owner\n', 'Page\n', 'Paint\n', 'Painting\n', 'Paper\n', 'Part\n', 'Passenger\n', 'Passion\n', 'Patience\n', 'Payment\n', 'Penalty\n', 'People\n', 'Percentage\n', 'Perception\n', 'Performance\n', 'Period\n', 'Permission\n', 'Person\n', 'Personality\n', 'Perspective\n', 'Philosophy\n', 'Phone\n', 'Photo\n', 'Physics\n', 'Piano\n', 'Picture\n', 'Pie\n', 'Piece\n', 'Pizza\n', 'Place\n', 'Plan\n', 'Platform\n', 'Player\n', 'Poem\n', 'Poet\n', 'Poetry\n', 'Point\n', 'Police\n', 'Policy\n', 'Politics\n', 'Pollution\n', 'Population\n', 'Position\n', 'Possession\n', 'Possibility\n', 'Post\n', 'Pot\n', 'Potato\n', 'Power\n', 'Practice\n', 'Preference\n', 'Preparation\n', 'Presence\n', 'Presentation\n', 'President\n', 'Pressure\n', 'Price\n', 'Priority\n', 'Problem\n', 'Procedure\n', 'Process\n', 'Product\n', 'Profession\n', 'Professor\n', 'Profit\n', 'Program\n', 'Promotion\n', 'Property\n', 'Proposal\n', 'Protection\n', 'Psychology\n', 'Purpose\n', 'Quality\n', 'Quantity\n', 'Queen\n', 'Question\n', 'Radio\n', 'Range\n', 'Rate\n', 'Ratio\n', 'Reaction\n', 'Reality\n', 'Reason\n', 'Reception\n', 'Recipe\n', 'Recognition\n', 'Recommendation\n', 'Record\n', 'Recording\n', 'Reflection\n', 'Refrigerator\n', 'Region\n', 'Relation\n', 'Relationship\n', 'Replacement\n', 'Republic\n', 'Reputation\n', 'Requirement\n', 'Research\n', 'Resolution\n', 'Resource\n', 'Response\n', 'Responsibility\n', 'Restaurant\n', 'Result\n', 'Revenue\n', 'Review\n', 'Revolution\n', 'Risk\n', 'River\n', 'Road\n', 'Rock\n', 'Role\n', 'Room\n', 'Rule\n', 'Safety\n', 'Salad\n', 'Salt\n', 'Sample\n', 'Satisfaction\n', 'Scale\n', 'Scene\n', 'School\n', 'Science\n', 'Screen\n', 'Secretary\n', 'Section\n', 'Sector\n', 'Security\n', 'Selection\n', 'Sense\n', 'Series\n', 'Service\n', 'Session\n', 'Setting\n', 'Shape\n', 'Share\n', 'Shirt\n', 'Side\n', 'Sign\n', 'Signature\n', 'Significance\n', 'Singer\n', 'Sir\n', 'Sister\n', 'Site\n', 'Situation\n', 'Size\n', 'Skill\n', 'Society\n', 'Software\n', 'Soil\n', 'Solution\n', 'Son\n', 'Song\n', 'Sound\n', 'Soup\n', 'Source\n', 'Space\n', 'Speaker\n', 'Speech\n', 'Sport\n', 'Square\n', 'Standard\n', 'Star\n', 'State\n', 'Statement\n', 'Steak\n', 'Step\n', 'Stock\n', 'Storage\n', 'Store\n', 'Story\n', 'Stranger\n', 'Strategy\n', 'Stress\n', 'Structure\n', 'Student\n', 'Studio\n', 'Study\n', 'Style\n', 'Subject\n', 'Success\n', 'Suggestion\n', 'Sun\n', 'Supermarket\n', 'Surgery\n', 'Sympathy\n', 'Syst\n', 'Table\n', 'Tale\n', 'Task\n', 'Tax\n', 'Tea\n', 'Teacher\n', 'Technology\n', 'Television\n', 'Temperature\n', 'Tennis\n', 'Tension\n', 'Term\n', 'Test\n', 'Thanks\n', 'Theory\n', 'Thing\n', 'Thought\n', 'Throat\n', 'Time\n', 'Tongue\n', 'Tool\n', 'Tooth\n', 'Top\n', 'Topic\n', 'Town\n', 'Trade\n', 'Tradition\n', 'Trainer\n', 'Training\n', 'Transportation\n', 'Truth\n', 'Two\n', 'Type\n', 'Uncle\n', 'Understanding\n', 'Union\n', 'Unit\n', 'University\n', 'User\n', 'Value\n', 'Variation\n', 'Variety\n', 'Vehicle\n', 'Version\n', 'Video\n', 'View\n', 'Village\n', 'Virus\n', 'Voice\n', 'Volume\n', 'War\n', 'Warning\n', 'Water\n', 'Way\n', 'Weakness\n', 'Wealth\n', 'Weather\n', 'Web\n', 'Wedding\n', 'Week\n', 'While\n', 'Wife\n', 'Wind\n', 'Winner\n', 'Woman\n', 'Wood\n', 'Word\n', 'Work\n', 'Worker\n', 'World\n', 'Writer\n', 'Writing\n', 'Year\n', 'Youth']



def dnd_rpg():
    character_number = int(input('wybierz liczbę postaci: '))

    def random_stat():
        stat = 0
        for i in range(0, 3):
            stat = stat + random.randint(1, 6)
        return stat + (level_number-1)

    for i in range(0, character_number):

        # determining the level of NPC
        random_percentage_level = random.randint(1, 100)
        if random_percentage_level <= 75:
            level = "chłop"
            level_number = 2
        elif random_percentage_level < 89:
            level = "najemnik"
            level_number = 3
        elif random_percentage_level <= 93:
            level = "zawodowiec"
            level_number = 4
        elif random_percentage_level <= 99:
            level = "weteran"
            level_number = 5
        else:
            level = "legenda"
            level_number = 6

        # determining the statistics of the NPC
        hp = (level_number - 1) * (3 * random.randint(4, 9))
        STR = random_stat()
        DEX = random_stat()
        CON = random_stat()
        INT = random_stat()
        WIS = random_stat()
        CHA = random_stat()
        wzrost = random.randint(150, 180)
        waga = random.randint(55, 100)
        wiek = random.randint(17, 60)

        random_name = random.randrange(len(names))
        name = names[random_name]
        name = name.replace('\n', '')

        # determining the weapon
        random_percentage_weapon = (5 * (level_number - 1)) + random.randint(1, 90)
        if random_percentage_weapon <= 30:
            waepon = "drewniana pałka 1k6"
        elif random_percentage_weapon <= 48:
            waepon = "łuk 1k6"
        elif random_percentage_weapon <= 58:
            waepon = "toporek 1k6"
        elif random_percentage_weapon <= 70:
            waepon = "oszczep 1k6"
        elif random_percentage_weapon <= 75:
            waepon = "kusza 1k8"
        elif random_percentage_weapon <= 84:
            waepon = "włócznia 1k6/1k8"
        elif random_percentage_weapon <= 90:
            waepon = "nadziak 1k8"
        elif random_percentage_weapon <= 93:
            waepon = "wielka maczuga 1k10"
        elif random_percentage_weapon <= 96:
            waepon = "miecz długi 1k8/1k10"
        elif random_percentage_weapon <= 99:
            waepon = "miecz dwuręczny 2k6"
        else:
            waepon = "lanca 1k12"

        # determining the armour
        random_percentage_armour = (5 * (level_number - 1)) + random.randint(1, 90)
        if random_percentage_armour <= 50:
            armour = "zwykłe ubrania 10 + ZR"
        elif random_percentage_armour <= 80:
            armour = "pancerz skórzany 12 + ZR"
        elif random_percentage_armour <= 95:
            armour = "pancerz ćwiekowany 14 + ZR(max 2)"
        elif random_percentage_armour <= 99:
            armour = "pancerz kolczy 16"
        else:
            armour = "zbroja płytowa 18"

        # determining the loot
        random_percentage_loot = (10 * (level_number - 1)) + random.randint(1, 100)
        if random_percentage_loot <= 50:
            loot = ""
        elif random_percentage_loot <= 60:
            loot = "oszczep 1k6"
        elif random_percentage_loot <= 75:
            loot = "tarcza (+2 do pancerza)"
        elif random_percentage_loot <= 85:
            loot = "miksturka +1k4 hp"
        elif random_percentage_loot <= 90:
            loot = "zwój z losowym zaklęciem"
        elif random_percentage_loot <= 95:
            loot = "mikstura +2k4 hp"
        elif random_percentage_loot <= 97:
            loot = "trucizna +1k6 dmg/dc 14 con"
        elif random_percentage_loot <= 99:
            loot = "broń lepszczej jakości +1"
        else:
            loot = "ogień w butelce 3k8 dmg"

        def printing_npc():
            print(name, " ", level)
            print("wzrost=", wzrost, "cm", " waga=", waga, " wiek=", wiek)
            print('hp = ', hp)
            print("siła = ", STR, "(", (STR-10) // 2, ")",
                  "\nzręczność = ", DEX, "(", (DEX-10) // 2, ")",
                  "\nkondycja = ", CON, "(", (CON-10) // 2, ")",
                  "\ninteligencja = ", INT, "(", (INT-10) // 2, ")",
                  '\nmądrość = ', WIS, "(", (WIS-10) // 2, ")",
                  '\ncharyzma = ', CHA, "(", (CHA-10) // 2, ")",)
            print("Pieniądze: ",
                  "\nmiedziaki: ", random.randint(0, 100),
                  "\nsrebrniki: ", (level_number - 1) * random.randint(0, 10),
                  "\nzłoto: ", (level_number - 2) * random.randint(0, 5))
            print("Przedmioty: ")
            print(armour)
            print(waepon)
            print(loot)
            for j in range(1, (level_number - 1) * random.randint(2, 6)):
                random_noun = random.randrange(len(nouns))
                noun = nouns[random_noun]
                noun = noun.replace('\n', ' ')
                print(noun, end="")

            print("\n****************************************")

        printing_npc()

dnd_rpg()
