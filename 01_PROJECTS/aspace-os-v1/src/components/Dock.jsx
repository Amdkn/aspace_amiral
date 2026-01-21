import React from 'react';
import { osDefinitions } from '../data/osDefinitions';

// Color class mapping for Tailwind purge safety
const colorClasses = {
  solar: 'bg-gradient-to-br from-solar-400 to-solar-600',
  nature: 'bg-gradient-to-br from-nature-400 to-nature-600',
  sky: 'bg-gradient-to-br from-sky-400 to-sky-600',
};

// Dock Component - Floating navigation bar
// Inspired by macOS dock & os.ryo.lu
// BMAD: Simple, Modular, Beautiful
export const Dock = ({ onOpenWindow }) => {
  return (
    <div className="fixed bottom-6 left-1/2 transform -translate-x-1/2 z-50">
      <div className="glass rounded-2xl px-4 py-3 flex items-center gap-3 shadow-2xl">
        {osDefinitions.map((os) => (
          <button
            key={os.id}
            onClick={() => onOpenWindow(os.id, os)}
            className={`
              group relative
              w-14 h-14 
              rounded-xl 
              ${colorClasses[os.color] || colorClasses.sky}
              hover:scale-110 
              active:scale-95
              transition-all duration-200 ease-out
              flex items-center justify-center
              text-2xl
              shadow-lg hover:shadow-xl
            `}
            title={os.description}
          >
            <span className="filter drop-shadow-sm">{os.icon}</span>
            
            {/* Tooltip */}
            <div className="absolute -top-12 left-1/2 transform -translate-x-1/2 opacity-0 group-hover:opacity-100 transition-opacity duration-200 pointer-events-none">
              <div className="glass px-3 py-1 rounded-lg whitespace-nowrap text-xs font-medium text-gray-800">
                {os.name}
              </div>
            </div>
          </button>
        ))}
      </div>
    </div>
  );
};
