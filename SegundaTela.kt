package com.example.geradordenumeroreal

import android.content.ClipData
import android.content.ClipboardManager
import android.content.Context
import android.content.Intent
import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.example.geradordenumeroreal.databinding.ActivitySegundaTelaBinding
import kotlin.random.Random

class SegundaTela : AppCompatActivity() {

    private lateinit var binding: ActivitySegundaTelaBinding

    private var numerosGerados = false

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        binding = ActivitySegundaTelaBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.limparBtn.isEnabled = false

        val gerarNumerosBtn: Button = findViewById(R.id.gerarNumerosBtn)
        val numerosGeradosTxt: TextView = findViewById(R.id.numerosGeradosTxt)

        gerarNumerosBtn.setOnClickListener {
            val listaNumeros = gerarNumeros()
            numerosGeradosTxt.text = listaNumeros.joinToString("\n")
            numerosGerados = true
            binding.limparBtn.isEnabled = true
            binding.copiarBtn.isEnabled = true
        }

        val copiarBtn: Button = findViewById(R.id.copiarBtn)

        copiarBtn.setOnClickListener {
            if (numerosGerados) {
                val listaNumeros = gerarNumeros()
                val numerosTexto = listaNumeros.joinToString("\n")

                val clipboardManager =
                    getSystemService(Context.CLIPBOARD_SERVICE) as ClipboardManager
                val clipData = ClipData.newPlainText("NumerosGerados", numerosTexto)
                clipboardManager.setPrimaryClip(clipData)

                Toast.makeText(this, "Números copiados para a área de transferência", Toast.LENGTH_SHORT)
                    .show()
            }

            else {
                Toast.makeText(this, "Por favor, gere números antes de copiar", Toast.LENGTH_SHORT).show()
                binding.copiarBtn.isEnabled = false
            }
        }


        binding.limparBtn.setOnClickListener {
            numerosGerados = false
            binding.limparBtn.isEnabled = false
            binding.numerosGeradosTxt.text = "Nenhum número gerado!"
        }

        binding.voltarBtn.setOnClickListener {
            val voltar = Intent(this, PrimeiraTela::class.java)
            startActivity(voltar)
        }
    }

    private fun gerarNumeros(): List<String> {
        val d = "wa.me/55"
        val c = "9"
        return List(10) {
            "$d${gerarA()}$c${gerarB()}"
        }
    }

    private fun gerarA(): String {
        return (0..1).map { Random.nextInt(10) }.joinToString("")
    }

    private fun gerarB(): String {
        return (0..7).map { Random.nextInt(10) }.joinToString("")
    }
}
