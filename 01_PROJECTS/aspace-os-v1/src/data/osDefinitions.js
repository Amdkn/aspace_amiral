// A'Space OS Definitions - V1
// Following BMAD-METHOD: Modular, Independent, Antifragile

export const osDefinitions = [
  {
    id: 'kernel',
    name: 'Kernel OS',
    icon: '⚙️',
    color: 'sky',
    description: '13th Doctor - Infrastructure & Context',
    defaultUrl: null, // Internal dashboard
    type: 'internal',
  },
  {
    id: 'ikigai',
    name: 'Ikigai OS',
    icon: '🎯',
    color: 'solar',
    description: 'La Raison d\'Être - Life Purpose & Vision',
    defaultUrl: null,
    type: 'internal',
  },
  {
    id: 'life',
    name: 'Life OS',
    icon: '🌿',
    color: 'nature',
    description: '11th Doctor - Life & Harmony',
    defaultUrl: null,
    type: 'internal',
  },
  {
    id: 'business',
    name: 'Business OS',
    icon: '💼',
    color: 'sky',
    description: '12th Doctor - Value & Projects',
    defaultUrl: null,
    type: 'internal',
  },
  {
    id: 'solarpunk',
    name: 'Solarpunk OS',
    icon: '🌞',
    color: 'solar',
    description: 'Vision Monde - Sustainable Future',
    defaultUrl: null,
    type: 'internal',
  },
];

// OS Data - Read from repository markdown files
export const osData = {
  kernel: {
    title: 'TARDIS CORE STATUS',
    status: 'operational',
    modules: [
      { name: 'Protocol Health', status: 'green' },
      { name: 'Context Load', status: 'green' },
      { name: 'Blueprint Factory', status: 'yellow' },
    ],
  },
  ikigai: {
    title: 'IKIGAI - La Raison d\'Être',
    pillars: [
      'Ce que j\'aime (Passion)',
      'Ce pour quoi je suis doué (Vocation)',
      'Ce dont le monde a besoin (Mission)',
      'Ce pour quoi je suis payé (Profession)',
    ],
    horizons: ['H1 (1 an)', 'H3 (3 ans)', 'H10 (10 ans)', 'H30 (30 ans)', 'H90 (90 ans)'],
  },
  life: {
    title: 'LIFE FLEET MONITOR',
    domains: [
      'Santé & Vitalité',
      'Mental & Émotionnel',
      'Partenaire & Amour',
      'Famille & Amis',
      'Mission & Carrière',
      'Finances & Liberté',
      'Fun & Aventure',
      'Environnement Physique',
    ],
  },
  business: {
    title: 'BUSINESS PULSE',
    organs: [
      'Growth (Marketing, Vente)',
      'Operations (Livraison, Qualité)',
      'Product (Innovation, R&D)',
      'Finance (Cashflow, P&L)',
      'People (Culture, Équipe)',
      'IT / Tech (Outils, IA)',
      'Legal / Admin (Conformité)',
    ],
  },
  solarpunk: {
    title: 'SOLARPUNK VISION',
    principles: [
      'Biomimétisme',
      'Circular Blue Economy',
      'Low Tech Acupuncture',
      'Meta-Science / Anti-Fragile',
      'Open Citizen Democracy',
    ],
  },
};
