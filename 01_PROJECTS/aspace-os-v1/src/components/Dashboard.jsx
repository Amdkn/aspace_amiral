import React from 'react';
import { osData } from '../data/osDefinitions';

// Dashboard Component - Internal OS Display
// BMAD: Data-driven, Fallback to local markdown/json
export const Dashboard = ({ osId }) => {
  const data = osData[osId];

  if (!data) {
    return (
      <div className="p-8 text-center">
        <div className="text-6xl mb-4">⚠️</div>
        <h2 className="text-xl font-semibold text-gray-700 mb-2">
          No data available
        </h2>
        <p className="text-gray-500">
          Dashboard configuration for {osId} not found.
        </p>
      </div>
    );
  }

  return (
    <div className="p-6 h-full overflow-y-auto">
      <h1 className="text-3xl font-bold mb-6 bg-gradient-to-r from-solar-600 to-sky-600 bg-clip-text text-transparent">
        {data.title}
      </h1>

      {/* Kernel OS Dashboard */}
      {osId === 'kernel' && (
        <div className="space-y-4">
          <div className="grid gap-3">
            {data.modules.map((module, idx) => (
              <div
                key={idx}
                className="glass rounded-lg p-4 flex items-center justify-between"
              >
                <span className="font-medium text-gray-700">{module.name}</span>
                <span
                  className={`px-3 py-1 rounded-full text-xs font-semibold ${
                    module.status === 'green'
                      ? 'bg-green-100 text-green-700'
                      : module.status === 'yellow'
                      ? 'bg-yellow-100 text-yellow-700'
                      : 'bg-red-100 text-red-700'
                  }`}
                >
                  {module.status.toUpperCase()}
                </span>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Ikigai OS Dashboard */}
      {osId === 'ikigai' && (
        <div className="space-y-6">
          <div>
            <h2 className="text-xl font-semibold mb-3 text-gray-700">
              4 Piliers de l'Ikigai
            </h2>
            <div className="grid gap-3">
              {data.pillars.map((pillar, idx) => (
                <div key={idx} className="glass rounded-lg p-4">
                  <p className="text-gray-700">{pillar}</p>
                </div>
              ))}
            </div>
          </div>
          <div>
            <h2 className="text-xl font-semibold mb-3 text-gray-700">
              5 Horizons Temporels
            </h2>
            <div className="grid gap-2">
              {data.horizons.map((horizon, idx) => (
                <div key={idx} className="glass rounded-lg p-3">
                  <p className="text-sm text-gray-600">{horizon}</p>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}

      {/* Life OS Dashboard */}
      {osId === 'life' && (
        <div>
          <h2 className="text-xl font-semibold mb-3 text-gray-700">
            8 Domaines de Vie
          </h2>
          <div className="grid gap-3">
            {data.domains.map((domain, idx) => (
              <div key={idx} className="glass rounded-lg p-4">
                <p className="text-gray-700">{domain}</p>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Business OS Dashboard */}
      {osId === 'business' && (
        <div>
          <h2 className="text-xl font-semibold mb-3 text-gray-700">
            7 Organes Business
          </h2>
          <div className="grid gap-3">
            {data.organs.map((organ, idx) => (
              <div key={idx} className="glass rounded-lg p-4">
                <p className="text-gray-700">{organ}</p>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Solarpunk OS Dashboard */}
      {osId === 'solarpunk' && (
        <div>
          <h2 className="text-xl font-semibold mb-3 text-gray-700">
            5 Principes Fondateurs
          </h2>
          <div className="grid gap-3">
            {data.principles.map((principle, idx) => (
              <div key={idx} className="glass rounded-lg p-4">
                <p className="text-gray-700">{principle}</p>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};
